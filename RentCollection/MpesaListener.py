from fastapi import FastAPI
from .DTOs import mpesa_apis_dtos

app = FastAPI()


# https://developer.safaricom.co.ke/APIs/CustomerToBusinessRegisterURL


# This is the URL that receives the confirmation request from API upon payment completion.
@app.get("/confirmation", response_model=mpesa_apis_dtos.mpesa_register_url)
def receive_mpesa_confirmation():
    return "Hello from MpesaListener.receive_mpesa_confirmation"


# This is the URL that receives the validation request from API upon payment submission.
# The validation URL is only called if the external validation on the registered shortcode is enabled.
# (By default External Validation is dissabled)
@app.get("/validation")
def validate_mpesa_transcation():
    return "Hello from MpesaListener.validate_mpesa_transcation"
