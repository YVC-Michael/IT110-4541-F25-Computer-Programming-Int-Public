###3. How Much Insurance?

### Many financial experts advise that property owners should insure their homes or buildings
### for at least 80 percent of the amount it would cost to replace the structure. Write a program
### that asks the user to enter the replacement cost of a building, then displays the minimum
### amount of insurance he or she should buy for the property.

# Global Variables
global replacement_cost
global minimum_insurance

# Named Constants
INSURANCE_PERCENTAGE = 0.80

def calculate_insurance():
    replacement_cost = float(input("Enter the replacement cost of the building: "))
    minimum_insurance = replacement_cost * INSURANCE_PERCENTAGE
    return minimum_insurance

def display_results():
    print()
    print(f"If the replacement cost of the building is: ${replacement_cost:,.2f}")
    print(f"The minimum amount of insurance you should buy for this property is: ${minimum_insurance:,.2f}")
    print()

# User Description
print()
print("This program will calculate the minimum amount of insurance")
print("you should buy for the property.")
print()

# Get user input for replacement cost
calculate_insurance()

# Display results
display_results()
print()
