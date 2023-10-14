import os

from dotenv import load_dotenv

load_dotenv()


class GlobalConfig:
    ENV: str = os.getenv("ENV", "default")
    DEBUG: bool = os.getenv("DEBUG", "false") == "true"
    assert isinstance(DEBUG, bool)
