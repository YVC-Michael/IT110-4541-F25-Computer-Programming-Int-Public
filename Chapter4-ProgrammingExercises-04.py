###Distance Traveled

### The distance a vehicle travels can be calculated as follows:
# distance = speed * time

### For example, if a train travels 40 miles per hour for three hours, the distance traveled is
### 120 miles. Write a program that asks the user for the speed of a vehicle (in miles per hour)
### and the number of hours it has traveled. It should then use a loop to display the distance
### the vehicle has traveled for each hour of that time period. Here is an example of the desired
### output:
# What is the speed of the vehicle in mph? 40 - Enter
# How many hours has it traveled? 3 - Enter
# Hour  Distance Traveled
# 1     40
# 2     80
# 3     120

# User Description
print()
print("This program will calculate the distance a vehicle travels based on speed and time.")
print()

# Get user input for speed and time
speed = int(input("Enter the speed of the vehicle in mph: "))
time = int(input("Enter the number of hours the vehicle has traveled: "))

# Calculate and display distance traveled for each hour
print()
print("Hour\tDistance Traveled (Miles)")
for hour in range(1, time + 1):
    distance = speed * hour
    print(f"{hour}\t{distance:>16}")
print()
