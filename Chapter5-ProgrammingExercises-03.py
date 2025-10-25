###3. How Much Insurance?

### Many financial experts advise that property owners should insure their homes or buildings
### for at least 80 percent of the amount it would cost to replace the structure. Write a program
### that asks the user to enter the replacement cost of a building, then displays the minimum
### amount of insurance he or she should buy for the property.

# Named Constants
INSURANCE_PERCENTAGE = 0.80

# Function to get user input
def get_user_input():
    replacement_cost = float(input("Enter the replacement cost of the building: "))
    return replacement_cost

# Function to calculate insurance
def calculate_insurance(replacement_cost):
    minimum_insurance = replacement_cost * INSURANCE_PERCENTAGE
    return replacement_cost, minimum_insurance

# Function to display results
def display_results(replacement_cost, minimum_insurance):
    print(f"\nIf the replacement cost of the building is: ${replacement_cost:,.2f}")
    print(f"The minimum amount of insurance you should buy for this property is: ${minimum_insurance:,.2f}\n")

# User Description
print("\nThis program will calculate the minimum amount of insurance")
print("you should buy for the property.\n")

# Get user input for replacement cost
replacement_cost = get_user_input()

# Calculate insurance
replacement_cost, minimum_insurance = calculate_insurance(replacement_cost)

# Display results
display_results(replacement_cost, minimum_insurance)
