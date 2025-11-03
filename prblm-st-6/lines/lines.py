
import sys
import os


def main():
    # Check for exactly one command-line argument
    if len(sys.argv) != 2:
        sys.exit("Usage: python lines.py filename.py")

    filename = sys.argv[1]

    # Check extension
    if not filename.endswith(".py"):
        sys.exit("Not a Python file")

    # Check file existence
    if not os.path.isfile(filename):
        sys.exit("File does not exist")

    try:
        with open(filename, "r", encoding="utf-8") as file:
            count = 0
            for line in file:
                stripped = line.strip()
                # Skip blank lines
                if not stripped:
                    continue
                # Skip comment lines
                if stripped.startswith("#"):
                    continue
                # Count everything else
                count += 1
    except Exception:
        sys.exit("Error reading file")

    print(count)


if __name__ == "__main__":
    main()
