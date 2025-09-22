import argparse
from pathlib import Path
from fandango import Fandango


def parse_fan_file(fan_file: Path, start_symbol: str = "<start>") -> Fandango:
    with open(fan_file, "r") as f:
        return Fandango(f, start_symbol=start_symbol)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--fan-file", type=Path, required=True)
    args = parser.parse_args()
    fan_file = args.fan_file

    fan = parse_fan_file(fan_file)

    print(str(next(fan.parse("123"))))


if __name__ == "__main__":
    main()
