###Sales Tax

### Write a program that will ask the user to enter the amount of a purchase. The program
### should then compute the state and county sales tax. Assume the state sales tax is 5 percent
### and the county sales tax is 2.5 percent. The program should display the amount of the
### purchase, the state sales tax, the county sales tax, the total sales tax, and the total of the
### sale (which is the sum of the amount of purchase plus the total sales tax).

### Hint: Use the value 0.025 to represent 2.5 percent, and 0.05 to represent 5 percent.

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
