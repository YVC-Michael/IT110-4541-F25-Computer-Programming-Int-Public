###4. Automobile Costs

### Write a program that asks the user to enter the monthly costs for the following expenses
### incurred from operating his or her automobile: loan payment, insurance, gas, oil, tires, and
### maintenance. The program should then display the total monthly cost of these expenses,
### and the total annual cost of these expenses.

# Named Constants
MONTHS_IN_YEAR = 12

# User Engagement
def get_values():
    print()
    print("This program will calculate the total monthly cost of these expenses,")
    print("and the total annual cost of these expenses.")
    print()
    loan_payment = float(input("Enter the monthly loan payment: "))
    insurance = float(input("Enter the monthly insurance: "))
    gas = float(input("Enter the monthly gas: "))
    oil = float(input("Enter the monthly oil: "))
    tires = float(input("Enter the monthly tires: "))
    maintenance = float(input("Enter the monthly maintenance: "))
    return loan_payment, insurance, gas, oil, tires, maintenance

# Calculate total monthly and annual cost
def calculate_cost(loan_payment, insurance, gas, oil, tires, maintenance):
    monthly_cost = loan_payment + insurance + gas + oil + tires + maintenance
    annual_cost = monthly_cost * MONTHS_IN_YEAR
    return monthly_cost, annual_cost

# Display results
def display_results(monthly_cost, annual_cost):
    print()
    print(f"The total monthly cost of these expenses is: ${monthly_cost:,.2f}")
    print(f"The total annual cost of these expenses is: ${annual_cost:,.2f}")
    print()

# Call function for monthly costs
loan_payment, insurance, gas, oil, tires, maintenance = get_values()

# Call function for monthly and annual cost
monthly_cost, annual_cost = calculate_cost(loan_payment, insurance, gas, oil, tires, maintenance)

# Call function for display results
display_results(monthly_cost, annual_cost)
