# 1.I first start with the guest list given that was given in the scenario.
guest_list = ["Chidi", "Lucas", "Miriam", "Jorge",
              "Gwen", "Nneka", "Egan", "Estella", "Josh"]

# 2.Second, I use the while loop to make it loop the menu forever until user stops.
while True:
    # \n means "new line" so it makes a blank line before the menu to make it look more neat.
    print("\nHow do you want to modify the list?")
    print("Select 1 - to add a name")  # The menu options to add.
    print("Select 2 - to remove a name")  # The menu options to remove.
    # The menu options to stop or quit the program.
    print("Select 3 - to quit the program")
    # Let the user choose the options above.
    user_choice = input("Choose an option from the given numbers above: ")

    # -------------------- ADD NAMES -------------------- (Just to not get it complicated)
    # If the user selects number two.
    if user_choice == "1":  # This will keep on adding until the user stops.
        while True:
            name = input(
                "Type the first name that you want to add (or type 'stop' to end): ")
            # This converts the user's input into lower case to make it less complicated and as well stops, If the user wants to stop adding.
            if name.lower() == "stop":
                break  # Stops
            # If the user types a given name, then that name will be placed at the last of the guest list.
            guest_list.append(name)
            print("You added:", name)  # Shows the name that the user add.
            # This lets the program count how many are in the list.
            print("People now:", len(guest_list))
            # This just prints the guest_list with the current updated one.
            print("Updated list:", guest_list)

            # Save the file
            # I then create a new file and write the given guest_list.
            with open("guest_list.txt", "w") as file:
                # It then loops through everything in the guest_list making the computer read all of it.
                for n in guest_list:
                    # It then write the name into the file with the "\n" which means making a new line so each name goes on it's own
                    file.write(n + "\n")
            # Then displays the text letting the user that it has been saved.
            print("List saved to file.")

    # -------------------- REMOVE NAMES -------------------- (Just to not get it complicated)
    # This checks if the user picked option 2 from the modify list.
    elif user_choice == "2":
        while True:  # Same as before, starts a loop that will keep running until the user stops.
            # Ask the user who she/he wants to remove
            name = input(
                "Type a name that you want to remove (or type 'stop' to end): ")
            # Same thing let's the user's input be converted into lowercase to not let the computer confused.
            if name.lower() == "stop":
                break  # Stops
            if name in guest_list:  # It checks if whatever the user type is inside the guest_list.
                guest_list.remove(name)  # If it sees it, it removes that name.
                # Then it lets the user know who he/she removed.
                print("You removed:", name)
            else:  # This will only run if the user inputted was not found.
                print("Name not found.")  # Displays and tell the user.

            # This then counts how many are in the guest_list.
            print("People now:", len(guest_list))
            # Displays and shows the latest updated list.
            print("Updated list:", guest_list)

            # Save the file
            # It opens or creates a new file called "guest.list.txt" and make it in write mode.
            with open("guest_list.txt", "w") as file:
                for n in guest_list:  # This then goes through each name in the list one by one.
                    # It then writes each of the name into the file and adds a new line same as before.
                    file.write(n + "\n")
            print("List saved to file.")  # Displays and let's the user know.

    # -------------------- QUIT -------------------- (Just to not get it complicated)
    elif user_choice == "3":  # Checks once again if the user selects number 3.
        # Once the user selects number three it then displays this.
        print("Oke' goodbye :)")
        break  # Then stop making it all end.
    else:
        # It displays if the user types other stuff other than in the modify list.
        print("Invalid choice, please choose from the given list numbers.")
