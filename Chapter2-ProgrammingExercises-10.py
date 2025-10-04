### Ingredient Adjuster

### A cookie recipe calls for the following ingredients:
## 1.5 cups of sugar
## 1 cup of butter
## 2.75 cups of flour

### The recipe produces 48 cookies with this amount of the ingredients. Write a program that
### asks the user how many cookies he or she wants to make, then displays the number of cups
### of each ingredient needed for the specified number of cookies.

# Named Constants
SUGAR_CUPS = 1.5
BUTTER_CUPS = 1
FLOUR_CUPS = 2.75
COOKIES = 48

# Print Prompt
print('Enter the number of cookies you want to make: ')
user_cookies = int(input())

# Calculate Ingredients
sugar_cups = (user_cookies / COOKIES) * SUGAR_CUPS
butter_cups = (user_cookies / COOKIES) * BUTTER_CUPS
flour_cups = (user_cookies / COOKIES) * FLOUR_CUPS

# Print Ingredients
print(f'The number of cups of sugar needed is: {sugar_cups:.3f}')
print(f'The number of cups of butter needed is: {butter_cups:.3f}')
print(f'The number of cups of flour needed is: {flour_cups:.3f}')
