from fastapi import APIRouter

router = APIRouter(
    prefix="/tenants",
    tags=['Tenants']
)


@router.get("/")
def get_all_tenants():
    return {"Get All Tenants"}
