###6. Calories from Fat and Carbohydrates

### A nutritionist who works for a fitness club helps members by evaluating their diets. As part
### of her evaluation, she asks members for the number of fat grams and carbohydrate grams
### that they consumed in a day. Then, she calculates the number of calories that result from
### the fat, using the following formula:
# calories from fat = fat grams * 9

### Next, she calculates the number of calories that result from the carbohydrates, using the
### following formula:
# calories from carbs = carb grams * 4

### The nutritionist asks you to write a program that will make these calculations.

# Named Constants
CALORIES_FROM_FAT = 9
CALORIES_FROM_CARBS = 4

# Function to get user input
def get_user_input():
    print("\nThis program will calculate the number of calories that result\nfrom the fat and carbohydrates you ate today.\n")
    fat_grams = float(input("Enter the number of fat grams you consumed today: "))
    carb_grams = float(input("Enter the number of carbohydrate grams you consumed today: "))
    return fat_grams, carb_grams

# Function to calculate calories from fat and carbohydrates
def calculate_calories(fat_grams, carb_grams):
    calories_from_fat = fat_grams * CALORIES_FROM_FAT
    calories_from_carbs = carb_grams * CALORIES_FROM_CARBS
    return calories_from_fat, calories_from_carbs

# Function to display results
def display_results(calories_from_fat, calories_from_carbs):
    print(f"\nThe number of calories from the fat you consumed today is:\n{calories_from_fat:.2f}")
    print(f"\nThe number of calories from the carbohydrates you consumed today is:\n{calories_from_carbs:.2f}\n")

# Program Execution
fat_grams, carb_grams = get_user_input()
calories_from_fat, calories_from_carbs = calculate_calories(fat_grams, carb_grams)
display_results(calories_from_fat, calories_from_carbs)
