import argparse
import pathlib
import sys


def process_path(path_s: str) -> None:
    path = pathlib.Path(path_s)

    if path.exists():
        print(f'[WARN] ignoring "{path}" because it already exists.', file=sys.stderr)

    if path_s.endswith("/"):
        path.mkdir(parents=True, exist_ok=True)
        return

    path.parent.mkdir(parents=True, exist_ok=True)
    path.touch(exist_ok=True)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="A simple script to painlessly create directories and files."
    )
    parser.add_argument(
        "-c",
        "--cwd",
        help="Set the working directory from which to do the operations.",
        default=".",
    )
    parser.add_argument("files", nargs="*")
    args = parser.parse_args()

    if args.cwd:
        import os

        print(
            "[INFO] Setting working direcotory to %s", repr(args.cwd), file=sys.stderr
        )
        os.chdir(args.cwd)

    if args.files:
        for path in args.files:
            process_path(path)


if __name__ == "__main__":
    main()
