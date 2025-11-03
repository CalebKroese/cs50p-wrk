import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # Regex for 0–255
    pattern = re.compile(r"""
        ^
        (25[0-5]|          # 250-255
         2[0-4][0-9]|      # 200-249
         1[0-9]{2}|        # 100-199
         [1-9]?[0-9])      # 0-99
        (\.
        (25[0-5]|
         2[0-4][0-9]|
         1[0-9]{2}|
         [1-9]?[0-9])
        ){3}
        $
    """, re.VERBOSE)

    return bool(pattern.match(ip))


if __name__ == "__main__":
    main()