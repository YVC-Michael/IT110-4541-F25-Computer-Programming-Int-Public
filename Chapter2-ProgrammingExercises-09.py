### Celsius to Fahrenheit Temperature Converter

### Write a program that converts Celsius temperatures to Fahrenheit temperatures. The
### formula is as follows:
### F = 9/5C + 32

### The program should ask the user to enter a Celsius temperature, then display the
### corresponding Fahrenheit temperature.

# Print Prompt
print('Enter the temperature in Celsius: ')
temp_celsius = float(input())

# Calculate Fahrenheit
temp_fahrenheit = (((9/5) * temp_celsius) + 32)

# Print Fahrenheit
print(f'The temperature in Fahrenheit is: {temp_fahrenheit:.2f}')
