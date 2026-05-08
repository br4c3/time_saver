import logging
import sys


def build_logger(level: str = "INFO") -> logging.Logger:
    logger = logging.getLogger("time_saver")
    
    # Prevent duplicated handlers
    if logger.handlers:
        return logger
    
    logger.setLevel(level.upper())
    logger.propagate = False
    
    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)

    return logger