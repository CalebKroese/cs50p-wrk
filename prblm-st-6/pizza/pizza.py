import sys
import os
import csv
from tabulate import tabulate


def main():
    # Check command-line args
    if len(sys.argv) != 2:
        sys.exit("Usage: python pizza.py filename.csv")

    filename = sys.argv[1]

    # Ensure .csv extension
    if not filename.endswith(".csv"):
        sys.exit("Not a CSV file")

    # Ensure file exists
    if not os.path.isfile(filename):
        sys.exit("File does not exist")

    try:
        with open(filename, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            table = list(reader)

            # First row = headers, rest = data
            headers = table[0]
            rows = table[1:]

            print(tabulate(rows, headers, tablefmt="grid"))

    except Exception:
        sys.exit("Error reading file")


if __name__ == "__main__":
    main()