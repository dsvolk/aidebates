import os

from dotenv import load_dotenv

load_dotenv()


class GlobalConfig:
    ENV: str = os.getenv("ENV", "default")
    DEBUG: bool = os.getenv("DEBUG", "false") == "true"
    assert isinstance(DEBUG, bool)

    N_SPEECHES = 3

    LLM_MODEL_NAMES = ["gpt-3.5-turbo", "gpt-4"]
    LLM_TEMPERATURE: float = float(os.getenv("LLM_TEMPERATURE", "0.7"))

    SAMPLE_MOTIONS = [
        "This house would ban the use of facial recognition technology",
        "This house believes that we should privatize the prison system",
        "Parliament members should be appointed by a lottery among the general population",
    ]

    GOV_PROMPT_TEMPLATE = """In parliament debates, you are the government and I am the opposition. You are arguing for the motion: {motion}. Your arguments are:

- It's good for the economy
- It's good for the environment
- It's good for the people

Be emotional and dramatic. Make sure to rebut the opposition's points in your speech.

Пиши на русском языке."""

    OPP_PROMPT_TEMPLATE = """In parliament debates, you are the opposition and I am the government. You are arguing against the motion: {motion}. Your arguments are:

- It's bad for the economy
- It's bad for the environment
- It's bad for the people

Be calm and logical. Make sure to rebut the government's points in your speech.

Пиши на русском языке."""

    GOV_AVATAR_PATH = "images/gov_avatar.png"
    OPP_AVATAR_PATH = "images/opp_avatar.png"
