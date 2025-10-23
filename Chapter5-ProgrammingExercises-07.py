###7. Stadium Seating

### There are three seating categories at a stadium. Class A seats cost $20, Class B seats cost
### $15, and Class C seats cost $10. Write a program that asks how many tickets for each class
### of seats were sold, then displays the amount of income generated from ticket sales.

# Named Constants
CLASS_A = 20
CLASS_B = 15
CLASS_C = 10

# Function to get user input
def get_user_input():
    print("\nThis program will calculate the amount of income generated from ticket sales.\n")
    tickets_class_a = int(input("Enter the number of Class A tickets sold: "))
    tickets_class_b = int(input("Enter the number of Class B tickets sold: "))
    tickets_class_c = int(input("Enter the number of Class C tickets sold: "))
    return tickets_class_a, tickets_class_b, tickets_class_c

# Function to calculate income
def calculate_income(class_a_tickets, class_b_tickets, class_c_tickets):
    income = (class_a_tickets * CLASS_A) + (class_b_tickets * CLASS_B) + (class_c_tickets * CLASS_C)
    return income

# Function to display results
def display_results(income):
    print(f"\nThe amount of income generated from ticket sales is: ${income:.2f}\n")

# Program Execution
class_a_tickets, class_b_tickets, class_c_tickets = get_user_input()
income = calculate_income(class_a_tickets, class_b_tickets, class_c_tickets)
display_results(income)
