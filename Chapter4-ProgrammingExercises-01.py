###Bug Collector

### A bug collector collects bugs every day for five days. Write a program that keeps a running
### total of the number of bugs collected during the five days. The loop should ask for the
### number of bugs collected for each day, and when the loop is finished, the program should
### display the total number of bugs collected.

# User Description
print("This program will calculate the total number of bugs collected over 5 days.")

# Initialize total bugs to 0
total_bugs = 0

# Loop through 5 days
for iteration in range(5):
    collected_bugs = int(input(f'Enter the number of bugs collected on day {iteration + 1}: '))
    total_bugs += collected_bugs

# Display total bugs collected
print(f'The total number of bugs collected over 5 days is: {total_bugs}')
