import sys
import random
import pyfiglet

def main():
    figlet = pyfiglet.Figlet()
    fonts = figlet.getFonts()

    # No extra arguments → random font
    if len(sys.argv) == 1:
        font = random.choice(fonts)

    # Two arguments → must be -f or --font + valid font name
    elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
        font = sys.argv[2]
        if font not in fonts:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")

    # Prompt user for input text
    text = input("Input: ")

    # Render with chosen font
    figlet = pyfiglet.Figlet(font=font)
    print("Output:")
    print(figlet.renderText(text))


if __name__ == "__main__":
    main()