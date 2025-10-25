###10. Feet to Inches

### One foot equals 12 inches. Write a function named feet_to_inches that accepts a number
### of feet as an argument and returns the number of inches in that many feet. Use the function
### in a program that prompts the user to enter a number of feet then displays the number of
### inches in that many feet.

# Named Constants
INCHES_PER_FOOT = 12

# Function to convert feet to inches
def feet_to_inches(feet):
    return feet * INCHES_PER_FOOT

# Function to get user input
def get_user_input():
    print("\nThis program will convert feet to inches.\n")
    feet = float(input("Enter the number of feet: "))
    return feet

# Function to display results
def display_results(feet, inches):
    print(f"\nThe number of inches in {feet} feet is: {inches:,.2f}")

# Program Execution
feet = get_user_input()
inches = feet_to_inches(feet)
display_results(feet, inches)
