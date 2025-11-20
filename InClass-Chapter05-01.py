### Write a function named times_ten. The function should accept an argument and
### display the product of its argument multiplied times 10.

def times_ten(number):
    return number * 10

def main():
    number = float(input("Enter a number: "))
    print(times_ten(number))

main()