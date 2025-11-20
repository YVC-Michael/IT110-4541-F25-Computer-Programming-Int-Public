### Write an if statement that assigns 20 to the variable y, and assigns 40 to the variable z
### if the variable x is greater than 100.

# Named Constants

x = int(input(f'Give me a number: '))

if x > 100:
    y = 20
    z = 40
    print(f'y={y} and z={z}')
else:
    print('Too Small')
    
