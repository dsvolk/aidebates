import os

from dotenv import load_dotenv

load_dotenv()


class GlobalConfig:
    ENV: str = os.getenv("ENV", "default")
    DEBUG: bool = os.getenv("DEBUG", "false") == "true"
    assert isinstance(DEBUG, bool)

    LLM_TEMPERATURE: float = float(os.getenv("LLM_TEMPERATURE", "0.7"))

    SAMPLE_MOTIONS = [
        "This house would ban the use of facial recognition technology",
        "This house believes that we should privatize the prison system",
        "Parliament members should be appointed by a lottery among the general population",
    ]

    GOV_AVATAR_PATH = "images/gov_avatar.png"
    OPP_AVATAR_PATH = "images/opp_avatar.png"
