###Tuition Increase

### At one college, the tuition for a full-time student is $8,000 per semester. It has been announced
### that the tuition will increase by 3 percent each year for the next 5 years. Write a program
### with a loop that displays the projected semester tuition amount for the next 5 years.

# Named Constants
TUITION_PER_SEMESTER = 8000
INCREASE_RATE = 0.03

# User Description
print()
print("This program will calculate the projected semester tuition amount for the next 5 years.")
print()

# Loop through years and calculate projected tuition
for year in range(5):
    projected_tuition = TUITION_PER_SEMESTER * (1 + INCREASE_RATE) ** year
    print(f"Year {year + 1}: {projected_tuition:,.2f}")
print()
