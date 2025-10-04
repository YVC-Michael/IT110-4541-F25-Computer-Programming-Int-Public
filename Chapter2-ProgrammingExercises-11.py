###Male and Female Percentages

### Write a program that asks the user for the number of males and the number of females 
### registered in a class. The program should display the percentage of males and females 
### in the class.

## Hint: Suppose there are 8 males and 12 females in a class. There are 20 students in the
## class. The percentage of males can be calculated as 8 ÷ 20 = 0.4, or 40%. The percentage
## of females can be calculated as 12 ÷ 20 = 0.6, or 60%.

# Print Prompt - Males
print('Enter the number of males in the class: ')
students_male = int(input())

# Print Prompt - Females
print('Enter the number of females in the class: ')
students_female = int(input())

# Calculate Total Students
students_total = students_male + students_female

# Calculate Percentages
male_percentage = (students_male / students_total) * 100
female_percentage = (students_female / students_total) * 100

# Print Percentages
print(f'The percentage of males in the class is: {male_percentage:.2f}%')
print(f'The percentage of females in the class is: {female_percentage:.2f}%')
