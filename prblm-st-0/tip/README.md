# Tip Calculator

## Description
This Python program calculates how much to leave as a tip based on the total meal cost and the desired tip percentage.
It demonstrates **functions**, **input handling**, and **string manipulation** in Python.

---

## How It Works
1. The program asks the user for:
   - The total meal cost (e.g. `$50.00`)
   - The desired tip percentage (e.g. `15%`)
2. It converts the inputs into floating-point numbers using two helper functions:
   - `dollars_to_float()` removes the `$` sign and converts to a float.
   - `percent_to_float()` removes the `%` sign and converts the value to a decimal.
3. It calculates the tip by multiplying the meal cost by the decimal percentage.
4. Finally, it prints the amount to leave as a tip, formatted to two decimal places.

---

## Example Usage

### Input:
How much was the meal? $50.00
What percentage would you like to tip? 15%

### Output:
Leave $7.50
