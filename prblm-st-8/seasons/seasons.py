from datetime import date, datetime
import inflect
import sys


def main():
    birth_str = input("Date of Birth: ")
    try:
        birth_date = date.fromisoformat(birth_str)
    except ValueError:
        sys.exit("Invalid date")

    today = date.today()
    minutes = minutes_lived(birth_date, today)

    p = inflect.engine()
    words = p.number_to_words(minutes, andword="").capitalize()
    print(f"{words} minutes")


def minutes_lived(birth_date, today):
    """Return number of minutes between birth_date and today."""
    if birth_date > today:
        return 0  # Optional: you could sys.exit("Invalid date") instead

    delta = today - birth_date
    return round(delta.days * 24 * 60)


if __name__ == "__main__":
    main()