1. Local / Azure ML setup
az extension add -n ml
az extension update -n ml
az login
az account show --output table
az group create --name training_group --location eastus

az ml workspace create `
  --name training-ws `
  --resource-group training_group `
  --location eastus
az configure --defaults group=training_group workspace=training-ws
2. Create compute
az ml compute create `
  --name cpu-cluster `
  --type amlcompute `
  --min-instances 0 `
  --max-instances 4
Verify:
az ml compute show --name cpu-cluster --output table
3. Train model
az ml job create --file job.yml
Verify job:
az ml job list --output table
az ml job show --name <job-name> --query status
Expected:
Completed
4. Register model
Use your completed job id:
az ml model create `
  --name loan-approval-model `
  --version 1 `
  --type custom_model `
  --path azureml://jobs/mighty_spade_m8vdp8ns6w/outputs/artifacts/paths/outputs/loan_model.pkl
Verify:
az ml model list --output table
Download test:
az ml model download `
  --name loan-approval-model `
  --version 1 `
  --download-path downloaded_model
5. Create batch endpoint
az ml batch-endpoint create `
  --name loanbatch01
Verify:
az ml batch-endpoint show `
  --name loanbatch01
Batch endpoints are for offline / asynchronous scoring, not real-time REST prediction. Invoking a batch endpoint creates an Azure ML job. 
6. Create batch deployment
az ml batch-deployment create `
  --file batch-deployment.yml
Verify deployment:
az ml batch-deployment show `
  --name blue `
  --endpoint-name loanbatch01
Set default deployment:
az ml batch-endpoint update `
  --name loanbatch01 `
  --set defaults.deploymentName=blue
Verify default:
az ml batch-endpoint show `
  --name loanbatch01 `
  --query defaults
7. Create batch input data
Your folder should be like:
batch_input/
  input.csv
Create data asset:
az ml data create `
  --name loan-batch-input `
  --version 1 `
  --type uri_folder `
  --path ./batch_input
Batch endpoints process data from cloud-accessible locations such as Azure ML data assets or datastores. 
Verify:
az ml data show `
  --name loan-batch-input `
  --version 1
8. Invoke batch endpoint
az ml batch-endpoint invoke `
  --name loanbatch01 `
  --deployment-name blue `
  --input azureml:loan-batch-input:1
This returns a job name. Save it.
Example:
batchjob-b2a1604c-0244-470d-9281-b5467fcccda5
9. Verify batch job
az ml job show `
  --name batchjob-b2a1604c-0244-470d-9281-b5467fcccda5 `
  --query status
Expected:
Completed
If failed:
az ml job show `
  --name batchjob-b2a1604c-0244-470d-9281-b5467fcccda5
Download output:
az ml job download `
  --name batchjob-b2a1604c-0244-470d-9281-b5467fcccda5 `
  --download-path batch_output
Check:
dir batch_output
10. Minimum verification checklist
Workspace created        ✅
Compute created          ✅
Training job completed   ✅
Model registered         ✅
Batch endpoint created   ✅
Batch deployment created ✅
Default deployment set   ✅
Input data asset created ✅
Endpoint invoked         ✅
Batch job completed      ✅
Output downloaded        ✅
11. GitHub service principal
az ad sp create-for-rbac `
  --name github-actions-sp `
  --role Contributor `
  --scopes /subscriptions/7d267e35-6fb2-4a8d-b9ce-c127545512c8 `
  --sdk-auth
Add the JSON output to GitHub:
Settings → Secrets and variables → Actions → New repository secret
Secret name:
AZURE_CREDENTIALS
Microsoft now recommends OIDC for GitHub Actions because it avoids long-lived secrets, but the service-principal secret method still works. 
12. GitHub CI/CD workflow
Create:
.github/workflows/azure-ml-batch-cicd.yml
name: Azure ML Batch CI/CD

on:
  push:
    branches:
      - master
  workflow_dispatch:

env:
  RESOURCE_GROUP: training_group
  WORKSPACE_NAME: training-ws
  COMPUTE_NAME: cpu-cluster
  MODEL_NAME: loan-approval-model
  ENDPOINT_NAME: loanbatch01
  DEPLOYMENT_NAME: blue

jobs:
  train-register-deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Azure login
        uses: azure/login@v2
        with:
          creds: ${{ secrets.AZURE_CREDENTIALS }}

      - name: Install Azure ML extension
        run: |
          az extension add -n ml -y
          az extension update -n ml

      - name: Set Azure ML defaults
        run: |
          az configure --defaults group=${{ env.RESOURCE_GROUP }} workspace=${{ env.WORKSPACE_NAME }}

      - name: Submit training job
        run: |
          az ml job create --file job.yml

      - name: Register model
        run: |
          az ml model create \
            --name ${{ env.MODEL_NAME }} \
            --version 1 \
            --type custom_model \
            --path azureml://jobs/mighty_spade_m8vdp8ns6w/outputs/artifacts/paths/outputs/loan_model.pkl

      - name: Create batch endpoint if not exists
        run: |
          az ml batch-endpoint show --name ${{ env.ENDPOINT_NAME }} || \
          az ml batch-endpoint create --name ${{ env.ENDPOINT_NAME }}

      - name: Create or update batch deployment
        run: |
          az ml batch-deployment create \
            --file batch-deployment.yml \
            --set name=${{ env.DEPLOYMENT_NAME }}

      - name: Set default deployment
        run: |
          az ml batch-endpoint update \
            --name ${{ env.ENDPOINT_NAME }} \
            --set defaults.deploymentName=${{ env.DEPLOYMENT_NAME }}

      - name: Create input data asset
        run: |
          az ml data create \
            --name loan-batch-input \
            --version 1 \
            --type uri_folder \
            --path ./batch_input

      - name: Invoke batch endpoint
        run: |
          az ml batch-endpoint invoke \
            --name ${{ env.ENDPOINT_NAME }} \
            --deployment-name ${{ env.DEPLOYMENT_NAME }} \
            --input azureml:loan-batch-input:1
Important: later replace the hardcoded job id mighty_spade_m8vdp8ns6w with dynamic job capture. For training class/demo, this version is okay first.

