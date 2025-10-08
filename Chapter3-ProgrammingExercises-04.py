###Roman Numerals

### Write a program that prompts the user to enter a number within the range of 1 through 10.
### The program should display the Roman numeral version of that number. If the number is
### outside the range of 1 through 10, the program should display an error message. The fol-
### lowing table shows the Roman numerals for the numbers 1 through 10:

#Named Constants
ROMAN_NUMERAL_1 = 'I'
ROMAN_NUMERAL_2 = 'II'
ROMAN_NUMERAL_3 = 'III'
ROMAN_NUMERAL_4 = 'IV'
ROMAN_NUMERAL_5 = 'V'
ROMAN_NUMERAL_6 = 'VI'
ROMAN_NUMERAL_7 = 'VII'
ROMAN_NUMERAL_8 = 'VIII'
ROMAN_NUMERAL_9 = 'IX'
ROMAN_NUMERAL_10 = 'X'

#Input
number_user = int(input('Enter a number within the range of 1 through 10: '))

#If-Elif-Else
if number_user == 1:
    print(ROMAN_NUMERAL_1)
elif number_user == 2:
    print(ROMAN_NUMERAL_2)
elif number_user == 3:
    print(ROMAN_NUMERAL_3)
elif number_user == 4:
    print(ROMAN_NUMERAL_4)
elif number_user == 5:
    print(ROMAN_NUMERAL_5)
elif number_user == 6:
    print(ROMAN_NUMERAL_6)
elif number_user == 7:
    print(ROMAN_NUMERAL_7)
elif number_user == 8:
    print(ROMAN_NUMERAL_8)
elif number_user == 9:
    print(ROMAN_NUMERAL_9)
elif number_user == 10:
    print(ROMAN_NUMERAL_10)

#Error Message
else:
    print(f'Error: Number {number_user} is outside the range of 1 through 10.')
    