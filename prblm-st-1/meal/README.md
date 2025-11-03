Meal Time Checker

Description

This Python program determines what meal time it is based on the user’s input. By converting the time into a floating-point number, it identifies whether it’s breakfast, lunch, dinner, or just a good time for a snack.



How It Works

The user enters a time in 24-hour format (e.g. 7:30, 12:00, 18:45).

The program passes that input to the convert() function:
    The function splits the time into hours and minutes.
    It converts both to integers and combines them into a float (e.g. 7:30 → 7.5).

The main function checks the converted time:
    7:00–8:00 → Breakfast Time
    12:00–13:00 → Lunch Time
    18:00–19:00 → Dinner Time
    Anything else → “Eat a snack I guess.”



Example Usage

Input:
What time is it? 7:30

Output:
Breakfast Time

Input:
What time is it? 12:45

Output:
Lunch Time

Input:
What time is it? 21:15

Output:
Eat a snack I guess.