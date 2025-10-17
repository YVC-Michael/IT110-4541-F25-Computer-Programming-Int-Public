###Calculating the Factorial of a Number

### In mathematics, the notation n! represents the factorial of the nonnegative integer n. The
### factorial of n is the product of all the nonnegative integers from 1 to n. For example,

# 7! = 1 * 2 * 3 * 4 * 5 * 6 * 7 = 5,040
# and
# 4! = 1 * 2 * 3 * 4 = 24

### Write a program that lets the user enter a nonnegative integer then uses a loop to calculate
### the factorial of that number. Display the factorial.

# User Description
print()
print("This program will calculate the factorial of a number.")
print()

# Get user input for number
number_input = int(input("Enter a nonnegative integer: "))
factorial = number_input
print()

# Loop through number and calculate factorial
for iteration in range(1, number_input):
    factorial *= iteration
    print(f"{factorial}")

# Display factorial
print()
print(f"The factorial of {number_input} is: {factorial}")
print()
