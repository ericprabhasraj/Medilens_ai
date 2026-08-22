import os
from dotenv import load_dotenv

load_dotenv()


def get_api_key():
    api_key = os.getenv("LLM_API_KEY")

    if not api_key:
        raise ValueError(
            "LLM_API_KEY is not configured. "
            "Add it to your .env file."
        )

    return api_key