import argparse


def parse_args(args=None):
    parser = argparse.ArgumentParser(description="Generate type annotations for Python files in the given path")
    parser.add_argument("path", help="Path to Python file or directory containing Python files")
    parser.add_argument("-i", "--in-place", help="Whether or not to make changes in place", action='store_true')

    return parser.parse_args(args=args)
