from fastapi import FastAPI
import consul
from contextlib import asynccontextmanager
from orderapp.configurations.config import CONSUL_HOST, CONSUL_PORT, SERVICE_NAME_1, SERVICE_ID_1, SERVICE_HOST_1, SERVICE_NAME_1, SERVICE_PORT_1, SERVICE_NAME_2, SERVICE_ID_2, SERVICE_HOST_2, SERVICE_PORT_2
# --------------------------------
# Lifespan (startup + shutdown)
# --------------------------------
@asynccontextmanager
async def lifespan(app: FastAPI):

    # startup
    c = consul.Consul(
        host=CONSUL_HOST,
        port=CONSUL_PORT
    )

    c.agent.service.register(
        name=SERVICE_NAME_1,
        service_id=SERVICE_ID_1,
        address=SERVICE_HOST_1,
        port=SERVICE_PORT_1,
        check={
            "http": f"http://{SERVICE_HOST_1}:{SERVICE_PORT_1}/health",
            "interval": "10s",
            "timeout": "5s"
        }
    )

    print("✅ Order service registered with Consul")

    yield

    # shutdown
    c.agent.service.deregister(SERVICE_ID_1)

    print("❌ Order service deregistered")



app = FastAPI(
    title="🛒 E-commerce API",
    description="API for managing e-commerce operations",
    version="1.0.0",lifespan=lifespan
)
@app.get("/health")
def health():
    return {
        "status": "UP"
    }
from orderapp.configurations.mysql_conf import engine, base
from orderapp.models.order import Order

# create tables
base.metadata.create_all(bind=engine)

# import router directly
from orderapp.controllers.order_controller import order_router

# debug routes
#for route in app.routes:
    #print("ROUTE:", route.path, route.methods)
app.include_router(order_router)
