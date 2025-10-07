###Day of the Week

### Write a program that asks the user for a number in the range of 1 through 7. The program
### should display the corresponding day of the week, where 1 = Monday, 2 = Tuesday,
### 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday. The program should
### display an error message if the user enters a number that is outside the range of 1 through 7.

#Named Constants
DAY_MONDAY = 1
DAY_TUESDAY = 2
DAY_WEDNESDAY = 3
DAY_THURSDAY = 4
DAY_FRIDAY = 5
DAY_SATURDAY = 6
DAY_SUNDAY = 7

#Input
day_user = int(input('Enter a number in the range of 1 through 7: '))

#If-Elif-Else
if day_user == DAY_MONDAY:
    print('Monday')
elif day_user == DAY_TUESDAY:
    print('Tuesday')
elif day_user == DAY_WEDNESDAY:
    print('Wednesday')
elif day_user == DAY_THURSDAY:
    print('Thursday')
elif day_user == DAY_FRIDAY:
    print('Friday')
elif day_user == DAY_SATURDAY:
    print('Saturday')
elif day_user == DAY_SUNDAY:
    print('Sunday')
else:
    print('Error: You entered a number that is outside the range of 1 through 7')
