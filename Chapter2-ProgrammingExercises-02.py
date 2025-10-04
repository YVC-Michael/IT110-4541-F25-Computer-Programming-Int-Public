###Sales Prediction

### A company has determined that its annual profit is typically 23 percent of total sales. Write a program that
### asks the user to enter the projected amount of total sales, then displays the VideoNote profit that will be 
### made from that amount.

### Hint: Use the value 0.23 to represent 23 percent.

# Named Constants
ANNUAL_PROFIT_PERCENTAGE = 0.23

# Print Prompt
print('Enter the projected amount of total sales: ')
total_sales = float(input())

# Calculate Total Profit
total_profit = total_sales * ANNUAL_PROFIT_PERCENTAGE

# Print Total Profit
print(f'The total profit is: ${total_profit:,.2f}')
