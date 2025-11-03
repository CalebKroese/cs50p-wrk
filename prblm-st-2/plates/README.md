Vanity Plate Validator

Description

This Python program checks whether a given license plate is valid based on a specific set of rules. It’s a great example of using string validation, loops, and conditional logic to enforce structured input.



Validation Rules

A valid plate must follow all of these:

1. Length: Between 2 and 6 characters (inclusive)
2. Start with letters: The first two characters must be alphabetic
3. Numbers (if any):
    -Must appear only at the end of the plate
    -The first number cannot be a 0
    -Once numbers begin, no more letters can follow
4. Allowed characters: Only letters and numbers — no punctuation, spaces, or symbols



Example Usage

Input:
Plate: CS50

Output:
Valid

Input:
Plate: C5S0

Output:
Invalid

Input:
Plate: OUTATIME

Output:
Invalid (Too long — more than 6 characters)