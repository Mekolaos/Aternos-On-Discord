from dotenv import load_dotenv
import os


def can_fire(func):
    if os.path.exists(os.path.relpath(".env")):
        func()
    else:
        print("Cannot find configuration file.")

    