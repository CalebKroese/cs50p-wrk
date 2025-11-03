import random


def main():
    # Get a valid level
    while True:
        try:
            n = int(input("Level: "))
            if n > 0:
                break
        except ValueError:
            pass  # ignore invalid input

    # Generate random number
    secret = random.randint(1, n)

    # Guessing loop
    while True:
        try:
            guess = int(input("Guess: "))
            if guess <= 0:
                continue  # only positive integers allowed

            if guess < secret:
                print("Too small!")
            elif guess > secret:
                print("Too large!")
            else:
                print("Just right!")
                break
        except ValueError:
            pass  # ignore invalid input


if __name__ == "__main__":
    main()