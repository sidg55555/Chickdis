import os
from box.exceptions import BoxValueError
import yaml
from Chickdis import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a yaml file and returns the contents as a ConfigBox object.

    Args:
        path_to_yaml (Path): Path to the yaml file.

    Raises:
        ValueError: If the file is empty.
        e: Any exception that occurs while reading the file.

    Returns:
        ConfigBox: Contents of the yaml file as a ConfigBox object.
    """
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            if content is None:
                raise ValueError(f"The file at {path_to_yaml} is empty.")
            return ConfigBox(content)
    except BoxValueError as e:
        raise ValueError(f"Error converting YAML to ConfigBox: {e}")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Creates directories if they do not exist.

    Args:
        path_to_directories (list): List of directory paths to create.
        verbose (bool, optional): If True, prints the created directories. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created at: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """Saves a dictionary as a JSON file.

    Args:
        path (Path): Path to the JSON file.
        data (dict): Dictionary to save.
    """
    with open(path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

    logger.info(f"JSON file saved at: {path}")

@ensure_annotations
def get_size(path: Path) -> str:
    """Returns the size of the file at the given path in KB.

    Args:
        path (Path): Path to the file.

    Returns:
        str: Size of the file in KB.
    """
    size_in_kb = round(os.path.getsize(path) / 1024, 2)
    return f"{size_in_kb} KB"