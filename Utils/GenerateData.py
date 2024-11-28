import os
from Managers.FileManager import get_json_path, write_to_file
from Utils.Config import DATA_DIR
from Utils.Types import TYPES


def generate_data_if_not_exist() -> None:
    """
    Generate Data dir and json files
    :return: None
    """
    if not resource_exists(DATA_DIR):
        os.mkdir(DATA_DIR)
    for name in TYPES:
        filepath = get_json_path(name)
        if resource_exists(filepath):
            continue
        write_to_file(filepath, "")
    return

def generate_content(name: str) -> str:
    pass

def resource_exists(resource_path: str) -> bool:
    """
    Check if resource exists
    :param resource_path: path to resource
    :return: whether resource exists
    """
    return os.path.exists(resource_path)