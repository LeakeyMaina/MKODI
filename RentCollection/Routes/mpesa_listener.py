
# https://developer.safaricom.co.ke/APIs/CustomerToBusinessRegisterURL

from fastapi import APIRouter
from ..Models.mpesa_dtos import dto_register_c2b_confirmation_urls

router = APIRouter(tags=['Listeners'])


# This is the URL that receives the confirmation request from API upon payment completion.
@router.get("/confirmation", response_model=dto_register_c2b_confirmation_urls)
def receive_mpesa_confirmation():
    return "Hello from MpesaListener.receive_mpesa_confirmation"


# This is the URL that receives the validation request from API upon payment submission.
# The validation URL is only called if the external validation on the registered shortcode is enabled.
# (By default External Validation is dissabled)
@router.get("/validation")
def validate_mpesa_transcation():
    return "Hello from MpesaListener.validate_mpesa_transcation"
