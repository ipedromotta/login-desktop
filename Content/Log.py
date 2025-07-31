import logging
from logging.handlers import RotatingFileHandler
from Model.Configuration import Configuration


_levels = {
    0: logging.NOTSET,
    1: logging.DEBUG,
    2: logging.INFO,
    3: logging.WARNING,
    4: logging.ERROR,
    5: logging.CRITICAL
}

_log_level = _levels.get(Configuration().log_level, logging.INFO)

# Handlers
stream_handler = logging.StreamHandler()
file_handler = RotatingFileHandler(
    filename='app.log',
    mode='a',
    maxBytes=1024 * 1024 * 5,  # 5 MB
    backupCount=3,
    encoding='utf-8'
)

# Formato de log
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger = logging.getLogger("app_logger")
logger.setLevel(_log_level)
logger.addHandler(stream_handler)
logger.addHandler(file_handler)
