import re
import sys


def main():
        print(count(input("Text: ")))


def count(s):
    """
    count occurrences of 'um' as a standalone word (case-insensitive).
    """
    return len(re.findall(r"\bum\b", s, re.IGNORECASE))


if __name__ == "__main__":
    main()