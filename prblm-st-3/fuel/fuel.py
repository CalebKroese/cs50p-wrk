def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            print(gauge(percentage))
            break
        except (ValueError, ZeroDivisionError):
            pass


def convert(fraction):
    try:
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)
    except Exception:
        raise ValueError("Invalid input, not integers")

    if y == 0:
        raise ZeroDivisionError("Denominator cannot be zero")

    if x <= 0 or y <= 0:
        raise ValueError("Numerator and denominator must be positive integers")

    if x > y:
        raise ValueError("Numerator cannot be greater than denominator")

    return round((x / y) * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()