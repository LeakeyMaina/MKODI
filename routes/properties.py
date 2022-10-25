from fastapi import APIRouter

router = APIRouter(
    prefix="/properties",
    tags=['Properties']
)


@router.get("/")
def get_all_properties():
    return {"Get All Properties"}
