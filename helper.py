from dotenv import load_dotenv
import os
import inspect
import asyncio


async def can_fire_async(func):
    if os.path.exists(os.path.relpath(".env")):
        return await func()
    else:
        print("Cannot find configuration file.")


def can_fire(func):
    if os.path.exists(os.path.relpath(".env")):
        return(func)
    else:
        print("Cannot find configuration file")
        