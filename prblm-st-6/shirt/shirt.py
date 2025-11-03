import sys
from PIL import Image, ImageOps


def main():
    # Check number of arguments
    if len(sys.argv) != 3:
        sys.exit("Usage: python shirt.py input output")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Allowed extensions
    valid_extensions = [".jpg", ".jpeg", ".png"]

    # Validate extensions (case-insensitive)
    if not any(input_file.lower().endswith(ext) for ext in valid_extensions):
        sys.exit("Invalid input file type")
    if not any(output_file.lower().endswith(ext) for ext in valid_extensions):
        sys.exit("Invalid output file type")

    # Ensure same extension
    if input_file.split(".")[-1].lower() != output_file.split(".")[-1].lower():
        sys.exit("Input and output have different extensions")

    try:
        # Open the shirt overlay
        shirt = Image.open("shirt.png")

        # Open the input image
        photo = Image.open(input_file)

        # Resize and crop input image to shirt’s size
        photo = ImageOps.fit(photo, shirt.size)

        # Overlay shirt.png on top of input
        photo.paste(shirt, (0, 0), shirt)

        # Save output
        photo.save(output_file)

    except FileNotFoundError:
        sys.exit("Input file does not exist")


if __name__ == "__main__":
    main()