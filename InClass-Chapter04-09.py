###Write code that prompts the user to enter a number in the range of 1 through 100 and
###validates the input.

number = int(input("Enter a number between 1 and 100: "))
while number < 1 or number > 100:
    number = int(input("Enter a number between 1 and 100: "))
print("The number is", number)

