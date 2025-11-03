###12. Average Steps Taken

### A Personal Fitness Tracker is a wearable device that tracks your physical activity, calories
### burned, heart rate, sleeping patterns, and so on. One common physical activity that most
### of these devices track is the number of steps you take each day.
### If you have downloaded this book’s source code from the Computer Science Portal, you
### will find a file named steps.txt in the Chapter 06 folder. (The Computer Science Portal
### can be found at www.pearsonhighered.com/gaddis.) The steps.txt file contains the
### number of steps a person has taken each day for a year. There are 365 lines in the file, and
### each line contains the number of steps taken during a day. (The first line is the number of
### steps taken on January 1st, the second line is the number of steps taken on January 2nd,
### and so forth.) Write a program that reads the file, then displays the average number of
### steps taken for each month. (The data is from a year that was not a leap year, so February
### has 28 days.)

# Hint/suggestion: for question number #12, assign months to named constants.
# Then, your write your program to pull from it to match and display the data from steps.txt file.

# Named constants
JAN_DAYS = 31
FEB_DAYS = 28
MARCH_DAYS = 31
APRIL_DAYS = 30
MAY_DAYS = 31
JUNE_DAYS = 30
JULY_DAYS = 31
AUG_DAYS = 31
SEPT_DAYS = 30
OCT_DAYS = 31
NOV_DAYS = 30
DEC_DAYS = 31

# Read the steps data
try:
    with open('Files/steps.txt', 'r') as steps_file:
        steps = [int(line) for line in steps_file]
    
    # Calculate and display average steps for each month using the named constants
    day_counter = 0
    print(f"January: {sum(steps[day_counter:day_counter+JAN_DAYS])/JAN_DAYS:.2f} steps")
    day_counter += JAN_DAYS
    
    print(f"February: {sum(steps[day_counter:day_counter+FEB_DAYS])/FEB_DAYS:.2f} steps")
    day_counter += FEB_DAYS
    
    print(f"March: {sum(steps[day_counter:day_counter+MARCH_DAYS])/MARCH_DAYS:.2f} steps")
    day_counter += MARCH_DAYS
    
    print(f"April: {sum(steps[day_counter:day_counter+APRIL_DAYS])/APRIL_DAYS:.2f} steps")
    day_counter += APRIL_DAYS
    
    print(f"May: {sum(steps[day_counter:day_counter+MAY_DAYS])/MAY_DAYS:.2f} steps")
    day_counter += MAY_DAYS
    
    print(f"June: {sum(steps[day_counter:day_counter+JUNE_DAYS])/JUNE_DAYS:.2f} steps")
    day_counter += JUNE_DAYS
    
    print(f"July: {sum(steps[day_counter:day_counter+JULY_DAYS])/JULY_DAYS:.2f} steps")
    day_counter += JULY_DAYS
    
    print(f"August: {sum(steps[day_counter:day_counter+AUG_DAYS])/AUG_DAYS:.2f} steps")
    day_counter += AUG_DAYS
    
    print(f"September: {sum(steps[day_counter:day_counter+SEPT_DAYS])/SEPT_DAYS:.2f} steps")
    day_counter += SEPT_DAYS
    
    print(f"October: {sum(steps[day_counter:day_counter+OCT_DAYS])/OCT_DAYS:.2f} steps")
    day_counter += OCT_DAYS
    
    print(f"November: {sum(steps[day_counter:day_counter+NOV_DAYS])/NOV_DAYS:.2f} steps")
    day_counter += NOV_DAYS
    
    print(f"December: {sum(steps[day_counter:day_counter+DEC_DAYS])/DEC_DAYS:.2f} steps")
    day_counter += DEC_DAYS

except:
    print("Error")
