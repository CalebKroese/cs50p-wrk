import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    """
    Convert 12-hour time ranges like '9:00 AM to 5 PM'
    into 24-hour format like '09:00 to 17:00'.
    Raise ValueError if invalid input.
    """

    # Regex allows optional minutes, mandatory AM/PM
    pattern = re.compile(
        r"^(\d{1,2})(?::(\d{2}))?\s(AM|PM)\sto\s(\d{1,2})(?::(\d{2}))?\s(AM|PM)$"
    )

    match = pattern.match(s)
    if not match:
        raise ValueError("Invalid format")

    h1, m1, ap1, h2, m2, ap2 = match.groups()

    # Defaults for minutes
    m1 = int(m1) if m1 else 0
    m2 = int(m2) if m2 else 0
    h1 = int(h1)
    h2 = int(h2)

    # Validate ranges
    if not (1 <= h1 <= 12) or not (0 <= m1 <= 59):
        raise ValueError("Invalid first time")
    if not (1 <= h2 <= 12) or not (0 <= m2 <= 59):
        raise ValueError("Invalid second time")

    t1 = to_24_hour(h1, m1, ap1)
    t2 = to_24_hour(h2, m2, ap2)

    return f"{t1} to {t2}"


def to_24_hour(h, m, ap):
    """Convert hour, minute, AM/PM to HH:MM in 24h format"""
    if ap == "AM":
        if h == 12:
            h = 0
    elif ap == "PM":
        if h != 12:
            h += 12
    return f"{h:02}:{m:02}"


if __name__ == "__main__":
    main()