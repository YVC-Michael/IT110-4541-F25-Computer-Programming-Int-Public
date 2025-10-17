###Budget Analysis

###Write a program that asks the user to enter the amount that he or she has budgeted for
### a month. A loop should then prompt the user to enter each of his or her expenses for the
### month and keep a running total. When the loop finishes, the program should display the
### amount that the user is over or under budget.

# User Description
print()
print("This program will calculate the amount that you are over or under budget.")
print()

# Initialize variables
monthly_expenses = 0
monthly_expenses_total = 0
continue_expenses = "Y"

# Get user input for budget and expenses
monthly_budget = float(input("Enter your monthly budget: "))

# Loop through expenses for 1 month
while continue_expenses == "Y":
    monthly_expenses = float(input(f"Enter an expense for this month: "))
    monthly_expenses_total += monthly_expenses
    continue_expenses = input("Do you have another expense? (Y/N): ")
    continue_expenses = continue_expenses.upper()

# Calculate and display amount over or under budget
if monthly_expenses_total > monthly_budget:
    print()
    print(f"You are over budget by ${monthly_expenses_total - monthly_budget:,.2f}")
    print()
else:
    print()
    print(f"You are under budget by ${monthly_budget - monthly_expenses_total:,.2f}")
    print()
