import os
from functools import reduce
from typing import List


def is_python_file(path: str) -> bool:
    return path.endswith(".py")


def find_python_files(path: str) -> List[str]:
    """
    Find all Python files in path in a recursive manner. If path points to one Python file, return that file.
    :param str path: Path to file or directory.
    :rtype: [str, ..]
    """
    if not os.path.exists(path):
        raise RuntimeError("Path {} does not exist".format(path))
    if os.path.isfile(path):
        return [path] if is_python_file(path) else []
    if os.path.isdir(path):
        return reduce(lambda files, child_path: files + find_python_files(child_path), os.listdir(path), [])


def get_functions_from_file(path: str):
    """
    Find all functions defined in the given Python file.
    :param path:
    :return:
    """

