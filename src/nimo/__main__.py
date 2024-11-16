import pathlib
import sys


def main() -> None:
    if len(sys.argv) == 1:
        print("Usage: [files...]")
        exit(1)

    for arg in sys.argv[1:]:
        path = pathlib.Path(arg)

        if path.exists():
            print(f"WARNING: ignoring \"{path}\" because it already exists.", file=sys.stderr)

        if arg.endswith("/"):
            path.mkdir(parents=True, exist_ok=True)
            continue

        path.parent.mkdir(parents=True, exist_ok=True)
        path.touch(exist_ok=True)

if __name__ == "__main__":
    main()
