def main():
    name = input("What is the Answer to the Great Question of Life, the Universe and Everthing? ")

    match name:
        case "42" | "Forty Two" | "forty-two":
            print("Yes")
        case _:
            print("No")


main()