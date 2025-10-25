###21. Rock, Paper, Scissors Game

### Write a program that lets the user play the game of Rock, Paper, Scissors against the
### computer. The program should work as follows:

# 1. When the program begins, a random number in the range of 1 through 3 is generated.
# If the number is 1, then the computer has chosen rock. If the number is 2, then the
# computer has chosen paper. If the number is 3, then the computer has chosen scissors.
# (Don’t display the computer’s choice yet.)
# 2. The user enters his or her choice of “rock,” “paper,” or “scissors” at the keyboard.
# 3. The computer’s choice is displayed.
# 4. A winner is selected according to the following rules:
## If one player chooses rock and the other player chooses scissors, then rock wins.
## (Rock smashes scissors.)
## If one player chooses scissors and the other player chooses paper, then scissors wins.
## (Scissors cuts paper.)
## If one player chooses paper and the other player chooses rock, then paper wins.
## (Paper wraps rock.)
## If both players make the same choice, the game must be played again to determine
## the winner.

# Flag to control the loop
PLAY_AGAIN = True

# Function to convert number to word
def convert_selection_to_word(number):
    if number == 1:
        return "ROCK"
    elif number == 2:
        return "PAPER"
    else:
        return "SCISSORS"

# Function to get user input
def get_input_user():
    choice_user = int(input("Enter your choice (rock = 1, paper = 2, or scissors = 3): "))
    if choice_user < 1 or choice_user > 3:
        print("\nInvalid choice. Please try again.")
        return get_input_user()
    choice_user = convert_selection_to_word(choice_user)
    return choice_user

# Function to get computer input
def get_input_computer():
    import random
    choice_computer = random.randint(1, 3)
    choice_computer = convert_selection_to_word(choice_computer)
    return choice_computer

#Function to determine results
def get_result(choice_user, choice_computer):
    if choice_user == choice_computer:
        winner = "TIE"
        PLAY_AGAIN = True
    elif (choice_user == "ROCK" and choice_computer == "SCISSORS") or (choice_user == "PAPER" and choice_computer == "ROCK") or (choice_user == "SCISSORS" and choice_computer == "PAPER"):
        winner = "YOU"
        PLAY_AGAIN = False
    else:
        winner = "ME"
        PLAY_AGAIN = False
    return winner, PLAY_AGAIN

# Function to display results
def display_results(choice_user, choice_computer, winner):
    print(f"\nYou chose: {choice_user}")
    print(f"The computer chose: {choice_computer}")
    print(f"The winner is: {winner}\n")
    if winner == "TIE":
        print("Play again!\n")
    else:
        print("Game Over!\n")

# Program Execution
print("\nThis program will play the game of Rock, Paper, Scissors against me.\n")
while PLAY_AGAIN:
    choice_user = get_input_user()
    choice_computer = get_input_computer()
    winner, PLAY_AGAIN = get_result(choice_user, choice_computer)
    display_results(choice_user, choice_computer, winner)
