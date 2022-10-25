from fastapi import FastAPI
from routes import landlords, properties, tenants

app = FastAPI()

app.include_router(landlords.router)
app.include_router(properties.router)
app.include_router(tenants.router)
