from dotenv import load_dotenv
import os
import inspect
import asyncio


async def can_fire(func):
    if os.path.exists(os.path.relpath(".env")):
        if asyncio.iscoroutinefunction(func):
            await func()
        else:
            func()
    else:
        print("Cannot find configuration file.")

    