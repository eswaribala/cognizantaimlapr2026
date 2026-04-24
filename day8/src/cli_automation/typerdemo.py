#create typer cli automation
import typer
app = typer.Typer()

@app.command()
def mysqlconfig(ipaddress: str, port: int, username: str, password: str):
    print(f"Configuring MySQL with IP address: {ipaddress}, Port: {port}, Username: {username}, Password: {password}")

@app.command()
def accessapi(endpoint: str, method: str):
    print(f"Accessing API Endpoint: {endpoint} with Method: {method}")

if __name__ == "__main__":
    app()