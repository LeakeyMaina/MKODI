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
    print(f'authorization_key = {settings.authorization_key}')
    print(f'authorization_key = {settings.base_url}')
    print(f'authorization_key = {settings.confirmation_url}')
    print(f'authorization_key = {settings.short_code}')
    print(f'authorization_key = {settings.response_type}')
    print(f'authorization_key = {settings.validation_url}')

async def test_mpesa_wrapper():
    api_wrapper = MpesaApiWrapper()
    return (await api_wrapper.get_access_token()) 

async def test_async_funcs():
    other_task_response = asyncio.create_task(other_task())
    access_token_response = asyncio.create_task(test_mpesa_wrapper())
    await other_task_response
    await access_token_response

    print(f'\nRECEIVED MPESA API RESPONSE... {access_token_response}\n')
    print(f'\n{other_task_response}\n')

   
test_config_env_file()
asyncio.run(test_async_funcs)
