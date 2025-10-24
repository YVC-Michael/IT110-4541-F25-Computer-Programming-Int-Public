###15. Test Average and Grade

### Write a program that asks the user to enter five test scores. The program should display a
### letter grade for each score and the average test score. Write the following functions in the
### program:

# calc_average. This function should accept five test scores as arguments and return the
# average of the scores.

# determine_grade. This function should accept a test score as an argument and return
# a letter grade for the score based on the following grading scale:

# Score       Letter Grade
# 90–100      A
# 80–89       B
# 70–79       C
# 60–69       D
# Below 60    F

# Named Constants
A = 90
B = 80
C = 70
D = 60

# Function to get user input
def get_user_input():
    print("\nThis program will calculate the average of five test scores and display the letter grade for each score.\n")
    score1 = float(input("Enter the first test score: "))
    score2 = float(input("Enter the second test score: "))
    score3 = float(input("Enter the third test score: "))
    score4 = float(input("Enter the fourth test score: "))
    score5 = float(input("Enter the fifth test score: "))
    return score1, score2, score3, score4, score5

# Function to calculate average
def calc_average(score1, score2, score3, score4, score5):
    scoreAverage = (score1 + score2 + score3 + score4 + score5) / 5
    return scoreAverage

# Function to determine grade
def determine_grade(score):
    if score >= A:
        return 'A'
    elif score >= B:
        return 'B'
    elif score >= C:
        return 'C'
    elif score >= D:
        return 'D'
    else:
        return 'F'

# Function to display results
def display_results(score1, score2, score3, score4, score5, scoreAverage):
    print(f"\nThe average of the five test scores is: {scoreAverage:,.2f}%")
    print(f"The letter grade for the average score is: {determine_grade(scoreAverage)}\n")
    print("The letter grade for each score is:")
    print(f"Score 1: {determine_grade(score1)}")
    print(f"Score 2: {determine_grade(score2)}")
    print(f"Score 3: {determine_grade(score3)}")
    print(f"Score 4: {determine_grade(score4)}")
    print(f"Score 5: {determine_grade(score5)}\n")

# Program Execution
score1, score2, score3, score4, score5 = get_user_input()
scoreAverage = calc_average(score1, score2, score3, score4, score5)
display_results(score1, score2, score3, score4, score5, scoreAverage)
