### Miles-per-Gallon
### A car’s miles-per-gallon (MPG) can be calculated with the following formula:
### MPG 5 Miles driven 4 Gallons of gas used

### Write a program that asks the user for the number of miles driven and the gallons of gas
### used. It should calculate the car's MPG and display the result.

# Print Prompt - Miles Driven
print('Enter the number of miles driven: ')
miles_driven = float(input())

# Print Prompt - Gallons of Gas Used
print('Enter the gallons of gas used: ')
gas_gallons_used = float(input())

# Calculate Miles per Gallon (mpg)
mpg = miles_driven / gas_gallons_used

# Print mpg
print(f'The car\'s MPG is: {mpg:.3f}')
