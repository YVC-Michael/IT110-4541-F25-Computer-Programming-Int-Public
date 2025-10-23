###1. Kilometer Converter

### Write a program that asks the user to enter a distance in kilometers, then converts that
### distance to miles. The conversion formula is as follows:

# Miles 5 Kilometers 3 0.6214

# Constants
KILOMETERS_TO_MILES = 0.6214

def convert_to_miles(kilometers):
    miles = kilometers * KILOMETERS_TO_MILES
    return miles

def display_results(kilometers, miles):
    print()
    print(f"{kilometers:.3f} kilometers is approximately {miles:.3f} miles.")
    print()

# User Engagement
print()
print("This program will convert kilometers to miles to the nearest thousandth.")
print()
kilometers = float(input("Enter a distance in kilometers: "))
print()

# Convert kilometers to miles
miles = convert_to_miles(kilometers)

# Display miles
display_results(kilometers, miles)
