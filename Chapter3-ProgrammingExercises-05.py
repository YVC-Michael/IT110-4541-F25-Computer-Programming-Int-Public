###Mass and Weight

### Scientists measure an object’s mass in kilograms and its weight in newtons. If you know
### the amount of mass of an object in kilograms, you can calculate its weight in newtons with
### the following formula:

# weight = mass * 9.8

### Write a program that asks the user to enter an object’s mass, then calculates its weight. If
### the object weighs more than 500 newtons, display a message indicating that it is too heavy.
### If the object weighs less than 100 newtons, display a message indicating that it is too light.

#Named Constants
FORMULA_MULTIPLIER = 9.8
WEIGHT_MIN = 100
WEIGHT_MAX = 500

#Input
mass_object = float(input('Enter the mass of the object in kilograms: '))

#Formula Math
weight_object = mass_object * FORMULA_MULTIPLIER

#If-Elif-Else
# Error Messages (Too Light/Heavy)
if weight_object < WEIGHT_MIN:
    print(f'Error: Object weighs {weight_object} newtons, which is too light.')
elif weight_object > WEIGHT_MAX:
    print(f'Error: Object weighs {weight_object} newtons, which is too heavy.')

# Output (Normal Weight)
else:
    print(f'Object weighs {weight_object} newtons.')
