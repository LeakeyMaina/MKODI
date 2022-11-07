from pydantic import BaseSettings, HttpUrl

class Settings(BaseSettings):
    base_url: str
    authorization_key: str
    short_code: str
    response_type: str
    confirmation_url: HttpUrl
    validation_url: HttpUrl

    class Config:
        env_file = ".env"


settings = Settings()
