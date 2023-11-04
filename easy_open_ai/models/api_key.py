import os

from dotenv import load_dotenv

try:
    # Get the current working directory
    current_directory = os.getcwd()
    dotenv_path = os.path.join(current_directory, ".env")

    load_dotenv(dotenv_path)  # Load variables from .env file
except:
    pass

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
