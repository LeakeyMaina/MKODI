from pydantic import BaseSettings, HttpUrl

from Models.mpesa_dtos import default_action


class Settings(BaseSettings):
    base_url: str
    authorization_key: str
    short_code: str
    response_type: default_action
    confirmation_url: HttpUrl
    validation_url: HttpUrl

    class Config:
        env_file = ".env"


settings = Settings()
