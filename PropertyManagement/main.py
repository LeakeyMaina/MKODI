from fastapi import FastAPI
from Routes import landlords, properties, tenants

app = FastAPI()

app.include_router(landlords.router)
app.include_router(properties.router)
app.include_router(tenants.router)


@app.get("/")
def root():
    return "Hello, Welcome to the MKODI Property Management API"
