🙂 Emoji Replacer
Description
This simple Python script takes a line of text from the user and automatically replaces emoticons with their corresponding emojis:

:) → 🙂
:( → 🙁
It’s a quick and fun way to add a touch of emotion to plain text messages.

How It Works
The program asks the user for input (a string of text).
It removes any extra spaces at the beginning or end of the input using .strip().
It replaces all instances of :) with 🙂.
It replaces all instances of :( with 🙁.
The updated text is then printed to the console.
Example Usage
Input:
Hello there! :)

Output:
Hello there! 🙂

Another Example:
Input:
I’m happy :) but also tired :(

Output:
I’m happy 🙂 but also tired 🙁