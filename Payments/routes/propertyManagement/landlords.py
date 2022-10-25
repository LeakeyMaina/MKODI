from fastapi import APIRouter, status

router = APIRouter(
    prefix="/landlords",
    tags=['Landlords']
)


@router.get("/", status_code=status.HTTP_200_OK)
def get_all_landlords():
    return {"Get All Landlords"}


@router.get("/{id}")
def get_landlord_by_id(id: int):
    return {f"Get landlord by ID {id}"}
