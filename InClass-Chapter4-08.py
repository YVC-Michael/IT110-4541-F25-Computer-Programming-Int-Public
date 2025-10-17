###Write code that prompts the user to enter a positive nonzero number and validates
###the input.

number = int(input("Enter a positive nonzero number: "))
while number <= 0:
    number = int(input("Enter a positive nonzero number: "))

print(f"The number is {number}")
