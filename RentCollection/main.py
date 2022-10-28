import asyncio
# import MpesaApiWrapper from Routes
from Routes.mpesa_api_wrapper import MpesaApiWrapper


async def other_task():
    for i in range(10):
        print(f"Running other tasks...{i}")
        await asyncio.sleep(0.1)
    return "Finished Other Task !!"


async def main():
    api_wrapper = MpesaApiWrapper()

    access_token_response = asyncio.create_task(
        api_wrapper.get_access_token())

    other_task_response = asyncio.create_task(other_task())

    print(f'\nRECEIVED MPESA API RESPONSE... {await access_token_response}\n')
    print(f'\n{await other_task_response}\n')

asyncio.run(main())
