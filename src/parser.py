import importlib
import inspect
import os
from functools import reduce
from typing import List, Callable


module_type = type(os)


def is_python_file(path: str) -> bool:
    return path.endswith(".py")


def find_python_files(path: str) -> List[str]:
    """
    Find all Python files in path in a recursive manner. If path points to one Python file, return that file.
    :param str path: Path to file or directory.
    :rtype: [str, ..]
    """
    path = os.path.relpath(os.path.abspath(path), os.getcwd())
    if not os.path.exists(path):
        raise RuntimeError("Path {} does not exist".format(path))
    if os.path.isfile(path):
        return [path] if is_python_file(path) else []
    if os.path.isdir(path):
        return reduce(lambda files, child_path: files + find_python_files("{}/{}".format(path, child_path)),
                      os.listdir(path), [])


def file_to_module(path: str) -> module_type:
    """
    Import a module from a given path if possible
    :param path: Path to a Python file
    :return:
    """
    return importlib.import_module(path.replace('/', '.').replace('.py', ''))


def is_function(obj, allow_builtin: bool=False) -> bool:
    """
    Check if the given object is a function
    :param obj: Possible function object
    :param allow_builtin: Whether or not to allow builtin functions
    :return: True if the object is a function
    """
    return inspect.isfunction(obj) or (allow_builtin and inspect.isbuiltin(obj))


def functions_in_module(module: module_type, include_builtins: bool=False) -> List[Callable]:
    """
    Retrieve all functions from a given module. Exclude builtin functions if specified
    :param module: Module to look for functions
    :param include_builtins: Whether or not to include builtin functions such as __hash__
    :return: List of functions in module
    """
    members = inspect.getmembers(module)
    return [obj for _, obj in members if is_function(obj, allow_builtin=include_builtins)]


def used_functions_in_function(f: Callable, include_unbound_members: bool=False) -> List[Callable]:
    """
    Find all functions that are being used in the given function.
    :param f: Function to check
    :param include_unbound_members: Whether or not to include unbound members in the result
    :return: List of functions that are called
    """
    closure_vars = inspect.getclosurevars(f)
    return [obj for obj in closure_vars.globals.values() if is_function(obj)]

