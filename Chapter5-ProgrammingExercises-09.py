###9. Monthly Sales Tax

### A retail company must file a monthly sales tax report listing the total sales for the month,
### and the amount of state and county sales tax collected. The state sales tax rate is 5 percent
### and the county sales tax rate is 2.5 percent. Write a program that asks the user to enter
### the total sales for the month. From this figure, the application should calculate and display
### the following:
# The amount of county sales tax
# The amount of state sales tax
# The total sales tax (county plus state)

# Named Constants
SALES_TAX_RATE_STATE = 0.05
SALES_TAX_RATE_COUNTY = 0.025

# Function to get user input
def get_user_input():
    print("\nThis program will calculate the amount of sales tax collected from a monthly sale.\n")
    sales_total = float(input("Enter the total sales for the month: "))
    return sales_total

# Function to calculate sales tax
def calculate_sales_tax(sales_total):
    sales_tax_state = sales_total * SALES_TAX_RATE_STATE
    sales_tax_county = sales_total * SALES_TAX_RATE_COUNTY
    sales_tax_total = sales_tax_state + sales_tax_county
    return sales_tax_state, sales_tax_county, sales_tax_total

# Function to display results
def display_results(sales_tax_state, sales_tax_county, sales_tax_total):
    print(f"\nThe amount of state sales tax is:\t$ {sales_tax_state:,.2f}")
    print(f"The amount of county sales tax is:\t$ {sales_tax_county:,.2f}")
    print(f"The total sales tax is:\t\t\t$ {sales_tax_total:,.2f}\n")

# Program Execution
sales_total = get_user_input()
sales_tax_state, sales_tax_county, sales_tax_total = calculate_sales_tax(sales_total)
display_results(sales_tax_state, sales_tax_county, sales_tax_total)
