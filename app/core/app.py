from app.core.config import Settings
from app.core.logger import build_logger


class App:
    def __init__(self):
        self.config = Settings()

        self.logger = build_logger(
            self.config.log_level
        )


app = App()