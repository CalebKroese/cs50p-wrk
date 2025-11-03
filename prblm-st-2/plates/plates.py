def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Length between 2 and 6
    if not (2 <= len(s) <= 6):
        return False

    # Must start with at least two letters
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    # Numbers, if present, must be at the end
    number_started = False
    for c in s:
        if c.isdigit():
            if not number_started:
                # first digit cannot be zero
                if c == "0":
                    return False
                number_started = True
        else:
            if number_started:
                # letter after numbers not allowed
                return False

    # No periods, spaces, or punctuation
    if not s.isalnum():
        return False

    return True


if __name__ == "__main__":
    main()