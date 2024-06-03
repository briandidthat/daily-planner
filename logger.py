import logging

from pythonjsonlogger import jsonlogger

handler = logging.StreamHandler(stream=None)
handler.setFormatter(
    jsonlogger.JsonFormatter(
        fmt="%(name)s %(asctime)s %(levelname)s %(message)s",
        rename_fields={"name": "logger", "asctime": "timestamp", "levelname": "level"},
    )
)


todist_logger = logging.getLogger("todoist-logger")
todist_logger.addHandler(handler)
todist_logger.setLevel(logging.INFO)
