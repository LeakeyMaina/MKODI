
import asyncio
from MpesaApiWrapper import MpesaApiWrapper
#from ..Tools.tools import read_environment_variable


async def other_task():
    for i in range(10):
        print(f"Running other tasks...{i}")
        await asyncio.sleep(0.1)
    return "Finished Other Task !!"


async def main():
    mpesa_wrapper = MpesaApiWrapper()

    # response = await asyncio.create_task(mpesa_wrapper.get_access_token())
    print(f'\n {(await asyncio.create_task(mpesa_wrapper.get_access_token()))}\n')
    print(f'\n {(await asyncio.create_task(other_task()))}\n')

# print(f'\n{await task2}\n')

# print(read_environment_variable("PATH"))

asyncio.run(main())
