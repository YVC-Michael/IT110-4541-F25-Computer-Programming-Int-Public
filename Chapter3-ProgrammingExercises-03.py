###Age Classifier

### Write a program that asks the user to enter a person’s age. The program should display
### a message indicating whether the person is an infant, a child, a teenager, or an adult.
### Following are the guidelines:

# If the person is 1 year old or less, he or she is an infant.
# If the person is older than 1 year, but younger than 13 years, he or she is a child.
# If the person is at least 13 years old, but less than 20 years old, he or she is a teenager.
# If the person is at least 20 years old, he or she is an adult.

#Named Constants
AGE_INFANT = 1
AGE_CHILD = 13
AGE_TEENAGER = 20

#Input
age_user = int(input('Enter a person\'s age: '))

#If-Elif-Else
if age_user <= AGE_INFANT:
    print('The person is an infant.')
elif age_user < AGE_CHILD:
    print('The person is a child.')
elif age_user < AGE_TEENAGER:
    print('The person is a teenager.')
else:
    print('The person is an adult.')