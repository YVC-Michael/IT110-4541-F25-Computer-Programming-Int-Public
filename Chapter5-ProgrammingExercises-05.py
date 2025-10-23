###5. Property Tax

### A county collects property taxes on the assessment value of property, which is 60 percent of
### the property’s actual value. For example, if an acre of land is valued at $10,000, its assess-
### ment value is $6,000. The property tax is then 72¢ for each $100 of the assessment value.
### The tax for the acre assessed at $6,000 will be $43.20. Write a program that asks for the
### actual value of a piece of property and displays the assessment value and property tax.

# Named Constants
PERCENTAGE_ASSESSMENT = 0.60
RATE_ASSESSMENT = 100
TAX_RATE_PROPERTY = 0.72

# Function to get user input
def get_user_input():
    print()
    actual_value = float(input("Enter the actual value of the property: "))
    return actual_value

# Function to calculate assessment value and property tax
def calculate_assessment_value(actual_value):
    assessment_value = actual_value * PERCENTAGE_ASSESSMENT
    property_tax = (assessment_value / RATE_ASSESSMENT) * TAX_RATE_PROPERTY
    return assessment_value, property_tax

# Function to display results
def display_results(actual_value, assessment_value, property_tax):
    print()
    print(f"The actual value of this property is: ${actual_value:,.2f}")
    print(f"The assessed value of this property is: ${assessment_value:,.2f}")
    print(f"The property tax for this property is: ${property_tax:,.2f}")
    print()

# Program Execution
actual_value = get_user_input()
assessment_value, property_tax = calculate_assessment_value(actual_value)
display_results(actual_value, assessment_value, property_tax)
