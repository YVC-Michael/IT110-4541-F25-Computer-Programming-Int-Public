###1. Kilometer Converter

### Write a program that asks the user to enter a distance in kilometers, then converts that
### distance to miles. The conversion formula is as follows:

# Miles 5 Kilometers 3 0.6214

# Constants
KILOMETERS_TO_MILES = 0.6214

# User Description
print()
print("This program will convert kilometers to miles.")
print()

# Get user input for kilometers
kilometers = float(input("Enter a distance in kilometers: "))

# Convert kilometers to miles
miles = kilometers * KILOMETERS_TO_MILES

# Display miles
print()
print(f"{kilometers} kilometers is equal to {miles:.3f} miles.")
print()
