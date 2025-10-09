### Write an if-else statement that determines whether the points variable is outside
### the range of 9 to 51. If the variable’s value is outside this range it should display
### “Invalid points.” Otherwise, it should display “Valid points.”

points = int(input('How many points? '))

if points < 9 or points > 51:
    print(f'Invalid points')
else:
    print(f'Valid points')
