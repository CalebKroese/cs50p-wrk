def main():
    # Prompt user
    expression = input("Expression: ").strip()

    # Split into parts
    x, y, z = expression.split()

    # Convert operands to integers
    x = int(x)
    z = int(z)

    # Evaluate based on operator
    if y == "+":
        result = x + z
    elif y == "-":
        result = x - z
    elif y == "*":
        result = x * z
    elif y == "/":
        result = x / z
    else:
        print("Invalid operator")
        return

    # Print formatted result
    print(f"{result:.1f}")


main()