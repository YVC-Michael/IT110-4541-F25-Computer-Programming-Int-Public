###Calories Burned

### Running on a particular treadmill you burn 4.2 calories per minute. Write a program that
### uses a loop to display the number of calories burned after 10, 15, 20, 25, and 30 minutes.

# User Description
print()
print("This program will calculate the number of calories burned after 10, 15, 20, 25, and 30 minutes.")
print()

#Name Constants
CALORIES_PER_MINUTE = 4.2

# Loop through calories burned for 10, 15, 20, 25, and 30 minutes
for iteration in range(10, 31, 5):
    calories_burned = iteration * CALORIES_PER_MINUTE
    print(f"After {iteration} minutes, you have burned {calories_burned} calories.")
print()
