Simple Arithmetic Expression Evaluator

Description

This Python program acts as a basic calculator that evaluates simple arithmetic expressions entered by the user. It supports addition, subtraction, multiplication, and division using clean and readable Python syntax.



How It Works

The program prompts the user to enter an expression (e.g. 3 + 4 or 10 / 2).

It removes extra spaces using .strip() and splits the input into three parts:
    x → the first number
    y → the operator
    z → the second number

It converts the numbers to integers and performs the correct operation based on the operator.

The result is displayed, formatted to one decimal place.



Example Usage

Input:
Expression: 3 + 5

Output:
8.0

Input:
Expression: 10 / 4

Output:
2.5

Input:
Expression: 7 - 2

Output:
5.0