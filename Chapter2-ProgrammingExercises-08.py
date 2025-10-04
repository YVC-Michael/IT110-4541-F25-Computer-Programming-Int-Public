### Tip, Tax, and Total

### Write a program that calculates the total amount of a meal purchased at a restaurant. The
### program should ask the user to enter the charge for the food, then calculate the amounts
### of a 18 percent tip and 7 percent sales tax. Display each of these amounts and the total.

# Named Constants
PERCENTAGE_TIP = 0.18
PERCENTAGE_SALES_TAX = 0.07

# Print Prompt - Meal Charge
print('Enter the charge for the food: ')
meal_charge = float(input())

# Calculate Tip
meal_tip = meal_charge * PERCENTAGE_TIP

# Calculate Tax
meal_sales_tax = meal_charge * PERCENTAGE_SALES_TAX

# Calculate Total
meal_total = meal_charge + meal_tip + meal_sales_tax

# Print Results
print(f'The charge for the food is:\t${meal_charge:8,.2f}')
print(f'The tip is:\t\t\t${meal_tip:8,.2f}')
print(f'The sales tax is:\t\t\t${meal_sales_tax:8,.2f}')
print(f'The total is:\t\t\t${meal_total:8,.2f}')
