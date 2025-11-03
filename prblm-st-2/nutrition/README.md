Fruit Calorie Finder

Description

This Python program lets you quickly look up the calorie count of a fruit from a predefined list. It demonstrates the use of dictionaries, string normalization, and conditional lookups in Python.



How It Works

1. The user is prompted to enter a fruit name.
2. The input is cleaned with .strip() (to remove extra spaces) and .lower() (to make it case-insensitive).
3. The program checks if the fruit exists in the dictionary.
4. If found, it prints the calorie amount per serving.
5. If not found, the program exits quietly (you can extend it to print a message like “Fruit not found”).



Example Usage

Input:
Item: Apple

Output:
Calories: 130

Input:
Item: watermelon

Output:
Calories: 80

Input:
Item: mango

Output:
(no output, since mango isn’t in the dictionary)