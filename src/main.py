from src.input import parse_args, find_python_files

if __name__ == "__main__":
    args = parse_args()
    python_files = find_python_files(args.path)
