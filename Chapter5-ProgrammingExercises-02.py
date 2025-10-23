###2. Sales Tax Program Refactoring

### Programming Exercise #6 in Chapter 2 was the Sales Tax program. For that exercise, you
### were asked to write a program that calculates and displays the county and state sales tax
### on a purchase. If you have already written that program, redesign it so the subtasks are in
### functions. If you have not already written that program, write it using functions.

# Named Constants
SALES_TAX_STATE = 0.05
SALES_TAX_COUNTY = 0.025

# Print Prompt
print('Enter the amount of a purchase: ')
purchase_amount = float(input())

# Calculate Sales Tax
sales_tax_state = purchase_amount * SALES_TAX_STATE
sales_tax_county = purchase_amount * SALES_TAX_COUNTY

# Calculate Total Sales Tax
sales_tax_total = sales_tax_state + sales_tax_county

# Calculate Total Sale
sale_total = purchase_amount + sales_tax_total

# Print Results
print(f'The amount of the purchase is:\t${purchase_amount:10,.2f}')
print(f'The state sales tax is:\t\t${sales_tax_state:10,.2f}')
print(f'The county sales tax is:\t\t${sales_tax_county:10,.2f}')
print(f'The total sales tax is:\t\t${sales_tax_total:10,.2f}')
print(f'The total of the sale is:\t\t${sale_total:10,.2f}')
