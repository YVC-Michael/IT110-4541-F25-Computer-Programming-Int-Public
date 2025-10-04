###Total Purchase

### A customer in a store is purchasing five items. Write a program that asks for the price of
### each item, then displays the subtotal of the sale, the amount of sales tax, and the total.
### Assume the sales tax is 7 percent.

# Named Constants
SALES_TAX = 0.07

# Print Prompts
priceOne = float(input('Enter the price of item 1: '))
priceTwo = float(input('Enter the price of item 2: '))
priceThree = float(input('Enter the price of item 3: '))
priceFour = float(input('Enter the price of item 4: '))
priceFive = float(input('Enter the price of item 5: '))

# Calculate Subtotal and Total
priceSubTotal = priceOne + priceTwo + priceThree + priceFour + priceFive

# Calculate Total
priceTotal = priceSubTotal * (1 + SALES_TAX)

# Print Subtotal and Total
print(f'The subtotal is ${priceSubTotal:.2f}')
print(f'The total is ${priceTotal:.2f}')
