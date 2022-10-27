import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    pass


def read_environment_variable(environment_variable):
    return os.getenv(environment_variable)
