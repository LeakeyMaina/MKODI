from fastapi import FastAPI
from PropertyManagement.routes import landlords, properties, tenants

app = FastAPI()

app.include_router(landlords.router)
app.include_router(properties.router)
app.include_router(tenants.router)
