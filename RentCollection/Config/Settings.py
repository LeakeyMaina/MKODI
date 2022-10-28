from pydantic import BaseSettings, HttpUrl
from RentCollection.DTOs.mpesa_apis_dtos import default_action
#import RentCollection.DTOs.mpesa_apis_dtos


class Settings(BaseSettings):
    AuthorizationKey: str
    ShortCode: str
    ResponseType: default_action
    ConfirmationURL: HttpUrl
    ValidationURL: HttpUrl

    class Config:
        env_file = ".env"
