from pprint import pformat
import logging


class CustomFormatter(logging.Formatter):
    blue = "\x1b[38;5;39m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format = "[%(asctime)s][%(levelname)s] %(message)s"

    FORMATS = {
        logging.DEBUG: format + reset,
        logging.INFO: blue + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.FATAL: bold_red + format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


logging.basicConfig(filename='test.log', encoding='utf-8', level=logging.DEBUG)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
Channel = logging.StreamHandler()
Channel.setLevel(logging.DEBUG)
Channel.setFormatter(CustomFormatter())
logger.addHandler(Channel)


def debug(msg: object) -> None:
    logger.debug(msg)


def info(msg: object) -> None:
    logger.info(msg)


def warn(msg: object) -> None:
    logger.warning(msg)


def fatal(msg: object) -> None:
    logger.fatal(msg)


def crit(msg: object) -> None:
    logger.critical(msg)


def data(msg: object) -> None:
    logger.info("\n%s", pformat(msg, indent=1, width=1))
