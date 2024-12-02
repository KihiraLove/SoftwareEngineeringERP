from datetime import datetime

from Utils import Config


def generate_time() -> datetime:
    return datetime.strptime(datetime.now().strftime(Config.TIME_FORMAT), Config.TIME_FORMAT)
