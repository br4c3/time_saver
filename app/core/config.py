import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    def __init__(self):
        self.discord_token = os.getenv(
            "DISCORD_TOKEN"
        )

        self.log_level = os.getenv(
            "LOG_LEVEL",
            "INFO"
        )