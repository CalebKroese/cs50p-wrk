import csv
from fpdf import FPDF
from datetime import datetime


def add_transaction(amount, category, description, file="budget_data.csv"):
    """
    Add a transaction (positive = income, nagative = expense)
    and save it to a CSV file.
    """
    try:
        amount = float(amount)
    except ValueError:
        raise ValueError("Amount must be a number")

    with open(file, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now().strftime("%Y-%m-%d"), amount, category, description])

    return True


def calculate_balance(file="budget_data.csv"):
    """
    Return the net balance by summing all transactions
    """
    try:
        with open(file, newline="") as f:
            reader = csv.reader(f)
            total = sum(float(row[1]) for row in reader)
        return round(total, 2)
    except FileNotFoundError:
        return 0.0


def get_summary_by_category(file="budget_data.csv"):
        """
        Return a dict of totals grouped by category.
        """
        summary = {}
        try:
            with open(file, newline="") as f:
                reader = csv.reader(f)
                for _, amount, category, _ in reader:
                    amount = float(amount)
                    summary[category] = summary.get(category, 0) + amount
            return summary
        except FileNotFoundError:
            return {}


def get_income_and_expenses(file="budget_data.csv"):
    """
    Separate income and expenses and return as two list tuples.
    """
    income = []
    expenses = []
    try:
        with open(file, newline="") as f:
            reader = csv.reader(f)
            for date, amount, category, desc in reader:
                amount = float(amount)
                if amount >= 0:
                    income.append((date, amount, category, desc))
                else:
                    expenses.append((date, amount, category, desc))
    except FileNotFoundError:
        pass
    return income, expenses


def export_pdf(file="budget_data.csv", output="budget_report.pdf"):
    """
    Export a clean PDF report using fpdf2
    """
    pdf = FPDF()
    pdf.add_page()

    # Header
    pdf.set_font("Helvetica", "B", 24)
    pdf.cell(0, 15, "Budget Report", ln=True, align="C")
    pdf.ln(5)

    # Summary
    pdf.set_font("Helvetica", "B", 14)
    balance = calculate_balance(file)
    pdf.cell(0, 10, f"Ovrerall Balance: ${balance:.2f}", ln=True, align="C")
    pdf.ln(5)

    income, expenses = get_income_and_expenses(file)

    # Income section
    pdf.set_text_color(34, 139, 34)  # Green
    pdf.set_font("Helvetica", "B", 16)
    pdf.cell(0, 10, "Income", ln=True)
    pdf.set_font("Helvetica", "", 12)
    pdf.set_text_color(0, 0, 0)

    if income:
        for date, amount, category, desc in income:
            pdf.cell(0, 8, f"{date} | {category}: ${amount:.2f} ({desc})", ln=True)
    else:
        pdf.cell(0, 8, " No income recorded.", ln=True)

    pdf.ln(8)

    # Expenses section
    pdf.set_text_color(220, 20, 60)  # Red
    pdf.set_font("Helvetica", "B", 16)
    pdf.cell(0, 10, "Expenses", ln=True)
    pdf.set_font("Helvetica", "", 12)
    pdf.set_text_color(0, 0, 0)

    if expenses:
        for date, amount, category, desc in expenses:
            pdf.cell(0, 8, f"{date} | {category}: ${amount:.2f} ({desc})", ln=True)
    else:
        pdf.cell(0, 8, "No expenses recorded.", ln=True)

    pdf.ln(8)

    # Category summary
    summary = get_summary_by_category(file)
    if summary:
        pdf.set_font("Helvetica", "B", 14)
        pdf.cell(0, 10, "Category Summary", ln=True)
        pdf.set_font("Helvetica", "", 12)
        for category, total in summary.items():
            pdf.cell(0, 8, f"{category}: ${total:.2f}", ln=True)


    pdf.output(output)
    return output




# ---------MAIN PROGRAM---------

def main():
    print("Weclome to your Budget Manager!")

    while True:
        print("Choose an option:")
        print("1. Add Transaction")
        print("2. View Balance")
        print("3. View Summary by Category")
        print("4. Export PDF Report")
        print("5. Exit")

        print("")
        choice = input("Enter 1-5: ")

        if choice == "1":
            print("---------------------------------------")
            amount = input("Enter amount(use negative for expenses): ")
            print("")
            category = input("Enter category(e.g., Food, Rent, Income): ")
            print("")
            desc = input("Enter a short description: ")
            try:
                add_transaction(amount, category, desc)
                print("-------------------------------")
                print("Transaction added successfully!")
                print("-------------------------------")
            except ValueError as e:
                print("-----------")
                print(f"Error: {e}")
                print("-----------")

        elif choice == "2":
            print("-----------------------------------------------------")
            print(f"Your current balance is : ${calculate_balance():.2f}")
            print("-----------------------------------------------------")

        elif choice == "3":
            summary = get_summary_by_category()
            if not summary:
                print("----------------------------")
                print("No transaction recorded yet.")
                print("----------------------------")
            else:
                print("--------------------")
                print("Summary by Category:")
                print("--------------------")
                for cat, total in summary.items():
                    sign = "+" if total >= 0 else "-"
                    print(f"{cat}: {sign}${abs(total):.2f}")
                print("--------------------")

        elif choice == "4":
            export_pdf()
            print("------------------------------------------")
            print("PDF report exported as 'budget_report.pdf'")
            print("------------------------------------------")

        elif choice == "5":
            print("------------------------------")
            print("Goodbye! Keep budgeting smart!")
            print("------------------------------")
            break

        else:
            print("---------------------------------")
            print("Invalid choise. Please try again.")
            print("---------------------------------")


if __name__ == "__main__":
      main()