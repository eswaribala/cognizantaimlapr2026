#create fast api main filefrom fastapi import FastAPI
from fastapi import client

from fastapi import FastAPI
from fastapi.concurrency import asynccontextmanager
app = FastAPI(title="Banking API", 
              description="API for banking application", version="1.0.0")

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    await client.admin.command("ping")
    print("✅ MongoDB connected")

    yield

    # Shutdown logic
    await client.close()
    print("❌ MongoDB connection closed")

#make api call to the customer controller

from bankingapp.controllers import account_controller

app.include_router(account_controller.router)

