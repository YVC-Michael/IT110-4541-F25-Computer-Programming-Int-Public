###Weight Loss

### If a moderately active person cuts their calorie intake by 500 calories a day, they can typi-
### cally lose about 4 pounds a month. Write a program that lets the user enter their starting
### weight, then creates and displays a table showing what their expected weight will be at the
### end of each month for the next 6 months if they stay on this diet.

# Named Constants
WEIGHT_LOSS_MONTHLY = 4

# User Description
print()
print("This program will calculate your expected weight over 6 months if you maintain your diet.")
print()

# Get user input for starting weight
starting_weight = float(input("Enter your current weight: "))
print()

# Loop through months and calculate expected weight
for month in range(6):
    expected_weight = starting_weight - (WEIGHT_LOSS_MONTHLY * (month + 1))
    print(f"Month {month + 1}: {expected_weight:>10.2f}")
print()
