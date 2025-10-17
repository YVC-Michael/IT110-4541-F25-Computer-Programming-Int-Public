###Write a loop that calculates the total of the following series of numbers:
### (1 / 3) + (2 / 29) + (3 / 28) + ... (30 / 1)

denominator = 30
total = 0
while denominator >= 1:
    total += denominator / (denominator + 2)
    denominator -= 1
print(f'The total is {total}')
    