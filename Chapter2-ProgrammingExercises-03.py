###Land Calculation

### One acre of land is equivalent to 43,560 square feet. Write a program that asks the user to
### enter the total square feet in a tract of land and calculates the number of acres in the tract.

### Hint: Divide the amount entered by 43,560 to get the number of acres.

# Named Constants
LAND_ACRE = 43560

# Print Prompt
print('Enter the total square feet in a tract of land: ')
total_square_feet = float(input())

# Calculate Total Acres
total_acres = total_square_feet / LAND_ACRE

# Print Total Acres
print(f'The number of acres in the tract is: {total_acres:.2f}')
