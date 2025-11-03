def main():
    groceries = {}

    while True:
        try:
            item = input().strip().lower()
            if item:  # ignore empty inputs
                groceries[item] = groceries.get(item, 0) + 1
        except EOFError:
            print()
            break

    for item in sorted(groceries):
        print(f"{groceries[item]} {item.upper()}")


if __name__ == "__main__":
    main()