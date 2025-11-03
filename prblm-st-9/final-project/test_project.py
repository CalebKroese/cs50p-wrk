import os
import csv
from project import add_transaction, calculate_balance, get_summary_by_category, get_income_and_expenses

TEST_FILE = "test_budget.csv"

def setup_function():
    with open(TEST_FILE, "w", newline="") as f:
        pass

def teardown_function():
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)

def test_add_function():
    assert add_transaction(100, "Income", "Paycheck", TEST_FILE)
    assert add_transaction(-25, "Food", "Lunch", TEST_FILE)
    with open(TEST_FILE) as f:
        rows = list(csv.reader(f))
        assert len(rows) == 2
        assert rows[0][2] == "Income"

def test_calculate_balance():
    add_transaction(100, "Income", "Paycheck", TEST_FILE)
    add_transaction(-40, "Groceries", "Food", TEST_FILE)
    assert calculate_balance(TEST_FILE) == 60.0

def test_get_summary_by_category():
    add_transaction(200, "Income", "Paycheck", TEST_FILE)
    add_transaction(-50, "Food", "Groceries", TEST_FILE)
    summary = get_summary_by_category(TEST_FILE)
    assert summary["Income"] == 200
    assert summary["Food"] == -50

def test_get_income_and_expenses():
    add_transaction(150, "Salary", "Monthly pay", TEST_FILE)
    add_transaction(-20, "Snacks", "Chips", TEST_FILE)
    income, expenses = get_income_and_expenses(TEST_FILE)
    assert len(income) == 1
    assert len(expenses) == 1