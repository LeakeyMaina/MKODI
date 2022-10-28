from pydantic import BaseSettings, HttpUrl

from ..Routes.mpesa_end_points import default_action


class Settings(BaseSettings):
    authorization_key: str
    short_code: str
    response_type: default_action
    confirmation_url: HttpUrl
    validation_url: HttpUrl

    class Config:
        env_file = ".env"


settings = Settings()
