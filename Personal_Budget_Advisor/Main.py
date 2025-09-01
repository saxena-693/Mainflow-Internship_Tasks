import os

DATA_FILE = "budget_data.txt"

def load_data():
    """Load previous transactions from file"""
    if not os.path.exists(DATA_FILE):
        return []
    transactions = []
    with open(DATA_FILE, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                t_type, category, amount = line.split(",")
                transactions.append({
                    "type": t_type,
                    "category": category,
                    "amount": float(amount)
                })
    return transactions


def save_data(transactions):
    """Save all transactions to file"""
    with open(DATA_FILE, "w") as file:
        for t in transactions:
            file.write(f"{t['type']},{t['category']},{t['amount']}\n")


def add_transaction(transactions, t_type):
    """Add income or expense entry"""
    try:
        category = input("Enter category (e.g., food, rent, salary): ").strip()
        amount = float(input("Enter amount: "))
        if amount <= 0:
            print("Amount must be positive.")
            return
        transactions.append({"type": t_type, "category": category, "amount": amount})
        save_data(transactions)
        print("Transaction added successfully.")
    except ValueError:
        print("Invalid input. Please enter a number for amount.")


def summarize(transactions):
    """Show total income, expenses, and category breakdown."""
    total_income = sum(t["amount"] for t in transactions if t["type"] == "income")
    total_expenses = sum(t["amount"] for t in transactions if t["type"] == "expense")
    savings = total_income - total_expenses

    print("\nSummary")
    print(f"Total Income:  ₹{total_income:.2f}")
    print(f"Total Expenses: ₹{total_expenses:.2f}")
    print(f"Savings:       ₹{savings:.2f}")


    category_expenses = {}
    for t in transactions:
        if t["type"] == "expense":
            category_expenses[t["category"]] = category_expenses.get(t["category"], 0) + t["amount"]

    if total_income > 0:
        print("\nCategory-wise Spending (% of income):")
        for cat, amt in category_expenses.items():
            percent = (amt / total_income) * 100
            print(f" - {cat}: ₹{amt:.2f} ({percent:.1f}%)")
    print("-------------------------\n")
    return total_income, total_expenses, savings, category_expenses


def give_suggestions(total_income, total_expenses, savings, category_expenses):
    """Rule-based budgeting suggestions."""
    print("Suggestions")

    if total_income == 0:
        print("No income recorded. Please add income first.")
        return

    if savings < 0:
        print("You are overspending! Try to cut unnecessary expenses.")
    elif savings < 0.1 * total_income:
        print("Try to save at least 10% of your income.")

    for cat, amt in category_expenses.items():
        if amt > 0.5 * total_income:
            print(f"Spending too much on {cat}. It's over 50% of your income!")
        elif amt > 0.3 * total_income:
            print(f"Consider reducing {cat} spending. It's above 30% of your income.")

    print("Track your spending regularly to build better saving habits.")
    print("----------------------------\n")

#Main Program
def main():
    transactions = load_data()

    while True:
        print("===== Personal Budget Advisor =====")
        print("1.Add Income")
        print("2.Add Expense")
        print("3.View Summary")
        print("4.Get Suggestions")
        print("5.Exit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_transaction(transactions, "income")
        elif choice == "2":
            add_transaction(transactions, "expense")
        elif choice == "3":
            total_income, total_expenses, savings, category_expenses = summarize(transactions)
        elif choice == "4":
            total_income, total_expenses, savings, category_expenses = summarize(transactions)
            give_suggestions(total_income, total_expenses, savings, category_expenses)
        elif choice == "5":
            print("Exiting. Stay mindful of your budget!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
