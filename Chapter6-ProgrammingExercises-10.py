###10. Golf Scores

### The Springfork Amateur Golf Club has a tournament every weekend. The club president
### has asked you to write two programs:
### 1. A program that will read each player’s name and golf score as keyboard input, then
### save these as records in a file named golf.txt. (Each record will have a field for the
### player’s name and a field for the player’s score.)
### 2. A program that reads the records from the golf.txt file and displays them.

# Function to create a new golf.txt file
def create_golf_file():
    file = open("./Files/golf.txt", "w")
    file.close()

# Function to select the program choice
def program_choice():
    print()
    program_choice = input("Press 1 to create a new golf.txt file or 2 to display the contents of the golf.txt file (1 or 2): ")
    if program_choice == "1":
        print()
        create_golf_file()
        add_golf_score()
    if program_choice =="2":
        print()
        display_golf_file()

# Function to add golf scores to the golf.txt file
def add_golf_score():
    file = open("./Files/golf.txt", "a")
    file.write(input("Enter player name: ") + " " + input("Enter player score: ") + "\n")
    print()
    add_another = input("Press 1 to add another player or any other key to exit: ")
    if add_another == "1":
        print()
        add_golf_score()
    else:
        file.close()
        print("\nGolf scores added to golf.txt file.\n")

# Function to display the contents of the golf.txt file
def display_golf_file():
    file = open("./Files/golf.txt", "r")
    print(file.read())
    file.close()

# Execute the program
program_choice()
