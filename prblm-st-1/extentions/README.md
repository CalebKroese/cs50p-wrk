# File Extension to Media Type Identifier

## Description
This Python program determines the **MIME type** (media type) of a file based on its extension.
It’s a practical example of using **dictionaries**, **string methods**, and **looping** to map file types to their correct media identifiers — commonly used in web development and file handling.

---

## How It Works
1. The program prompts the user to enter a filename (e.g. `photo.jpg` or `document.pdf`).
2. It removes any leading/trailing whitespace and converts the input to lowercase.
3. It compares the file’s extension against a predefined dictionary of known file types.
4. If a match is found, it prints the corresponding **MIME type**.
5. If no match is found, it defaults to `application/octet-stream`, a general-purpose binary type.

---

## Example Usage

### Input:
File name: picture.JPG

### Output:
image/jpeg

---

### Input:
File name: notes.txt

### Output:
text/plain

---

### Input:
File name: archive.unknown

### Output:
application/octet-stream
