Greeting Value Calculator

Description

This Python program assigns a monetary “value” to a user’s greeting based on how polite it sounds. It’s a fun exercise in string handling, conditional logic, and function design in Python.



How It Works

The user is prompted to enter a greeting.

The program passes that greeting to the value() function.

The greeting is converted to lowercase for consistency.

The value is determined by these rules:
    If the greeting starts with "hello" → returns 0
    Else if the greeting starts with "h" → returns 20
    Otherwise → returns 100

The result is printed to the console.



Example Usage

Input:
Greeting: Hello there

Output:
0

Input:
Greeting: Hi!

Output:
20

Input:
Greeting: Good morning

Output:
100