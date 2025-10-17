###Average Rainfall

### Write a program that uses nested loops to collect data and calculate the average rainfall over
### a period of years. The program should first ask for the number of years. The outer loop will
### iterate once for each year. The inner loop will iterate twelve times, once for each month.
### Each iteration of the inner loop will ask the user for the inches of rainfall for that month.
### After all iterations, the program should display the number of months, the total inches of
### rainfall, and the average rainfall per month for the entire period.

# User Description
print()
print("This program will calculate the average rainfall over a period of years.")
print()

# Initialize variables
total_rainfall = 0

# Get user input for number of years
total_years = int(input("Enter the number of years: "))

# Loop through years and months
for year in range(total_years):
    for month in range(12):
        rainfall = float(input(f"Enter the rainfall for month {month + 1} of year {year + 1}: "))
        total_rainfall += rainfall

# Calculate and display average rainfall
average_rainfall = total_rainfall / (total_years * 12)

# Display results
print()
print("Results:")
print(f"The total number of months is: {total_years * 12}")
print(f"The total inches of rainfall is: {total_rainfall:,.3f}")
print(f"The average rainfall per month is: {average_rainfall:,.2f}")
print()
