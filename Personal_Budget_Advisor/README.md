## Personal Budget Advisor :-
A simple command-line Personal Budget Advisor built in Python that helps you track income, expenses, analyze spending habits, and get saving suggestions.
This project stores your financial data locally in a text file (budget_data.txt) and provides a rule-based suggestion system to improve budgeting habits.

## Features :-
-  Add Income entries
-  Add Expenses with categories (e.g., food, rent, travel)
-  View Summary:
   -  Total income
   -  Total expenses
   -  Net savings
   -  Category-wise spending with percentages
-  Get Suggestions:
   -  Detect overspending
   -  Reminders to save at least 10% of income
   -  Warn if a category exceeds 30% or 50% of total income
-  Persistent Storage:
   -  Data is saved in budget_data.txt so that records are not lost between runs


## Project Structure :-
-  ├── budget_advisor.py   #Main program
-  ├── budget_data.txt     #Stores income/expense records (auto-created)
-  └── README.md           #Project documentation

## How to Run :-
-  Clone / Download this repository.
-  Make sure you have Python 3.x installed.
-  Run the program:
  -  python budget_advisor.py
  -  Follow the on-screen menu:

## Personal Budget Advisor :-
1. Add Income
2. Add Expense
3. View Summary
4. Get Suggestions
5. Exit


## Restrictions :-
-  No external libraries like pandas or numpy used.
-  Entirely built using Python’s built-in features.
