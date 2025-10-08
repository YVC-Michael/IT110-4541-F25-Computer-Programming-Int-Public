###Restaurant Selector

### You have a group of friends coming to visit for your high school reunion, and you want
### to take them out to eat at a local restaurant. You aren’t sure if any of them have dietary
### restrictions, but your restaurant choices are as follows:

# Joe’s Gourmet Burgers—Vegetarian: No, Vegan: No, Gluten-Free: No
# Main Street Pizza Company—Vegetarian: Yes, Vegan: No, Gluten-Free: Yes
# Corner Café—Vegetarian: Yes, Vegan: Yes, Gluten-Free: Yes
# Mama’s Fine Italian—Vegetarian: Yes, Vegan: No, Gluten-Free: No
# The Chef’s Kitchen—Vegetarian: Yes, Vegan: Yes, Gluten-Free: Yes
# Write a program that asks whether any members of your party are vegetarian, vegan, or
# gluten-free, to which then displays only the restaurants to which you may take the group.

### Here is an example of the program’s output:
# Is anyone in your party a vegetarian? yes Enter
# Is anyone in your party a vegan? no Enter
# Is anyone in your party gluten-free? yes Enter

## Here are your restaurant choices:
# Main Street Pizza Company
# Corner Cafe
# The Chef's Kitchen

### Here is another example of the program’s output:
# Is anyone in your party a vegetarian? yes Enter
# Is anyone in your party a vegan? yes Enter
# Is anyone in your party gluten-free? yes Enter

## Here are your restaurant choices:
# Corner Cafe
# The Chef's Kitchen

#Flag Variable
vegetarian = False
vegan = False
gluten_free = False

#Named Constants
RESTAURANT_1 = 'Joe’s Gourmet Burgers'
RESTAURANT_2 = 'Main Street Pizza Company'
RESTAURANT_3 = 'Corner Café'
RESTAURANT_4 = 'Mama’s Fine Italian'
RESTAURANT_5 = 'The Chef’s Kitchen'

#Input - Vegetarian
vegetarian_party = input('Is anyone in your party a vegetarian? (yes/no): ')
if vegetarian_party == 'yes':
    vegetarian = True

#Input - Vegan
vegan_party = input('Is anyone in your party a vegan? (yes/no): ')
if vegan_party == 'yes':
    vegan = True

#Input - Gluten-Free
gluten_free_party = input('Is anyone in your party gluten-free? (yes/no): ')
if gluten_free_party == 'yes':
    gluten_free = True

#Output - Restaurant Choices
print('\nHere are your restaurant choices:')

#No Dietery Restrictions
if vegetarian == False and vegan == False and gluten_free == False:
    print(RESTAURANT_1)
    print(RESTAURANT_2)
    print(RESTAURANT_3)
    print(RESTAURANT_4)
    print(RESTAURANT_5)

#Vegetarian Only
elif vegetarian == True and vegan == False and gluten_free == False:
    print(RESTAURANT_2)
    print(RESTAURANT_3)
    print(RESTAURANT_4)
    print(RESTAURANT_5)

#Vegetarian & Vegan
elif vegetarian == True and vegan == True and gluten_free == False:
    print(RESTAURANT_5)

#Vegetarian & Gluten-Free
elif vegetarian == True and vegan == False and gluten_free == True:
    print(RESTAURANT_2)
    print(RESTAURANT_3)
    print(RESTAURANT_5)

#Vegetarian, Vegan, and Gluten-Free 
elif vegetarian == True and vegan == True and gluten_free == True:
    print(RESTAURANT_5)

#Vegan Only
elif vegetarian == False and vegan == True and gluten_free == False:
    print(RESTAURANT_5)

#Vegan & Gluten-Free
elif vegetarian == False and vegan == True and gluten_free == True:
    print(RESTAURANT_5)

#Gluten-Free Only
elif vegetarian == False and vegan == False and gluten_free == True:
    print(RESTAURANT_2)
    print(RESTAURANT_3)
    print(RESTAURANT_5)
