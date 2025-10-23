###2. Sales Tax Program Refactoring

### Programming Exercise #6 in Chapter 2 was the Sales Tax program. For that exercise, you
### were asked to write a program that calculates and displays the county and state sales tax
### on a purchase. If you have already written that program, redesign it so the subtasks are in
### functions. If you have not already written that program, write it using functions.

# Named Constants
SALES_TAX_STATE = 0.05
SALES_TAX_COUNTY = 0.025

# Function to calculate tax and total
def calculate_sales_tax(purchase_amount):
    sales_tax_state = purchase_amount * SALES_TAX_STATE
    sales_tax_county = purchase_amount * SALES_TAX_COUNTY
    sales_tax_total = sales_tax_state + sales_tax_county
    purchase_total = purchase_amount + sales_tax_total
    return sales_tax_state, sales_tax_county, sales_tax_total, purchase_total

# Function to print results
def print_results(purchase_amount, sales_tax_state, sales_tax_county, sales_tax_total, purchase_total):
    print(f'The amount of the purchase is:\t\t${purchase_amount:10,.2f}')
    print(f'The state sales tax is:\t\t\t${sales_tax_state:10,.2f}')
    print(f'The county sales tax is:\t\t${sales_tax_county:10,.2f}')
    print()
    print(f'The total sales tax is:\t\t\t${sales_tax_total:10,.2f}')
    print(f'The total of the sale is:\t\t${purchase_total:10,.2f}')
    print()

# User Prompt
print()
purchase_amount = float(input("Enter the amount of a purchase: "))
print()

# Call function to calculate tax
sales_tax_state, sales_tax_county, sales_tax_total, purchase_total = calculate_sales_tax(purchase_amount)

# Call function to print results
print_results(purchase_amount, sales_tax_state, sales_tax_county, sales_tax_total, purchase_total)
