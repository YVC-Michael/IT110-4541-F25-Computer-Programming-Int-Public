### Write a function named times_ten that accepts a number as an argument. When the
### function is called, it should return the value of its argument multiplied times 10.

number = float(input("Enter a number: "))
result = times_ten(number)
print(result)

def times_ten(number):
    return number * 10
