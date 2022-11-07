import asyncio

# import MpesaApiWrapper from Routes
from Routes.mpesa_api_wrapper import MpesaApiWrapper
from Config.config import settings


async def other_task():
    for i in range(10):
        print(f"Running other tasks...{i}")
        await asyncio.sleep(0.1)
    return "Finished Other Task !!"


def test_config_env_file():
    print(f"authorization_key = {settings.authorization_key}")
    print(f"base_url = {settings.base_url}")
    print(f"confirmation_url = {settings.confirmation_url}")
    print(f"short_code = {settings.short_code}")
    print(f"response_type = {settings.response_type}")
    print(f"validation_url = {settings.validation_url}")


async def get_mpesa_access_token():
    mpesa_api_wrapper = MpesaApiWrapper()
    return await mpesa_api_wrapper.get_access_token()


async def demo_async_funcs():
    access_token_response = asyncio.create_task(get_mpesa_access_token())
    other_task_response = asyncio.create_task(other_task())

    print(f"\n<----RECEIVED MPESA API RESPONSE... {await access_token_response}\n")
    print(f"\n{await other_task_response}\n")


asyncio.run(demo_async_funcs())
