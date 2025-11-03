CamelCase to snake_case Converter

Description

This Python program converts a camelCase variable name into snake_case. It’s a simple and effective demonstration of string iteration, case checking, and string building in Python.



How It Works

-The program prompts the user to enter a variable name in camelCase format (e.g. thisIsAnExample).
-It loops through each character:
    -If the character is uppercase, it adds an underscore (_) followed by the lowercase version of that letter.
    -If it’s lowercase, it adds the character as is.
-It prints the converted snake_case version.



Example Usage

Input:
camelCase: thisIsAnExample

Output:
snake_case: this_is_an_example

Input:
camelCase: helloWorld

Output:
snake_case: hello_world

Input:
camelCase: myVariableName

Output:
snake_case: my_variable_name