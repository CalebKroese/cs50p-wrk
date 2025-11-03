Coin Payment Simulator

Description

This Python program simulates inserting coins into a vending machine until an item costing 50 cents is paid for. It’s a beginner-friendly example of loops, conditionals, and input validation in Python.

How It Works

1. The total amount due starts at 50 cents.
2. The user is repeatedly prompted to insert a coin.
3. Only coins of 25¢, 10¢, or 5¢ are accepted.
4. Each valid coin reduces the remaining amount due.
5. Once the amount due reaches 0 or less, the program prints the change owed (if the user overpaid).



Example Usage

Example 1 – Exact Payment

Amount Due: 50 Insert Coin: 25 Amount Due: 25 Insert Coin: 25 Change Owed: 0

Example 2 – Overpayment

Amount Due: 50 Insert Coin: 25 Amount Due: 25 Insert Coin: 10 Amount Due: 15 Insert Coin: 25 Change Owed: 10