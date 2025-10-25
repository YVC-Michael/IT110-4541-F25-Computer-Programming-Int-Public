###1. Kilometer Converter

### Write a program that asks the user to enter a distance in kilometers, then converts that
### distance to miles. The conversion formula is as follows:

# Miles 5 Kilometers 3 0.6214

# Constants
KILOMETERS_TO_MILES = 0.6214

# Function to convert kilometers to miles
def convert_to_miles(kilometers):
    miles = kilometers * KILOMETERS_TO_MILES
    return miles

# Function to display results
def display_results(kilometers, miles):
    print(f"\n{kilometers:.3f} kilometers is approximately {miles:.3f} miles.\n")

# Get user input
print("\nThis program will convert kilometers to miles to the nearest thousandth.")
kilometers = float(input("\nEnter a distance in kilometers: "))

# Call function to convert kilometers to miles
miles = convert_to_miles(kilometers)

# Call function to display results
display_results(kilometers, miles)
