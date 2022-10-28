from enum import Enum
from pydantic import BaseSettings, HttpUrl


# This parameter specifies what is to happen if for any reason the validation URL is nor reachable.
# Note that, This is the default action value that determines what MPesa will do in the scenario that your endpoint is unreachable or is unable to respond on time.
# Only two values are allowed: Completed or Cancelled.
# Completed means MPesa will automatically complete your transaction, whereas
# Cancelled means MPesa will automatically cancel the transaction, in the event MPesa is unable to reach your Validation URL.
class default_action(Enum):
    Completed = "Completed"
    Canceled = "Canceled"


class register_c2b_confirmation_urls(BaseSettings):
    "ShortCode": 123456
    "ResponseType": default_action
    "ConfirmationURL": HttpUrl
    "ValidationURL": HttpUrl
