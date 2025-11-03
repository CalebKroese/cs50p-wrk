def main():
    names = []

    # Keep prompting until EOF (Ctrl-D on Mac/Linux, Ctrl-Z on Windows)
    try:
        while True:
            name = input("Name: ")
            names.append(name)
    except EOFError:
        pass

    # Build the farewell string
    print(f"Adieu, adieu, to {format_names(names)}")


def format_names(names):
    n = len(names)

    if n == 1:
        return names[0]
    elif n == 2:
        return f"{names[0]} and {names[1]}"
    else:
        return f"{', '.join(names[:-1])}, and {names[-1]}"


if __name__ == "__main__":
    main()