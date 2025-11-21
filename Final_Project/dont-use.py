from pathlib import Path  # Added to build a save path relative to this file.

# 1.I first start with the guest list given that was given in the scenario.
guest_list = ["Chidi", "Lucas", "Miriam", "Jorge",
              "Gwen", "Nneka", "Egan", "Estella", "Josh"]

GUEST_FILE = Path(__file__).with_name("guest_list.txt")  # Keeps saves next to the script.


def save_guest_list():
    """Persist the guest list to disk once per add/remove session."""
    with GUEST_FILE.open("w", encoding="utf-8") as file:
        for name in guest_list:
            file.write(name + "\n")
    print(f"List saved to file: {GUEST_FILE}")  # Added feedback with file location.


def normalize(name_input):
    """Clean up user input and prevent blank additions."""
    return name_input.strip()


def find_matching_name(candidate):
    """Locate an existing name ignoring case so remove/add checks are consistent."""
    candidate_lower = candidate.lower()
    for stored in guest_list:
        if stored.lower() == candidate_lower:
            return stored
    return None

try:
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
                normalized_name = normalize(name)  # Removes extra spaces before storing.
                if normalized_name.lower() == "stop":
                    break  # Stops
                if not normalized_name:
                    print("Please enter a non-empty name.")  # Prevents blank entries.
                    continue
                if find_matching_name(normalized_name):
                    print("That name is already on the list.")  # Avoid duplicate entries.
                    continue
                # If the user types a given name, then that name will be placed at the last of the guest list.
                guest_list.append(normalized_name)
                print("You added:", normalized_name)  # Shows the name that the user add.
                # This lets the program count how many are in the list.
                print("People now:", len(guest_list))
                # This just prints the guest_list with the current updated one.
                print("Updated list:", guest_list)

                add_more = input("Add another? (y/n): ").strip().lower()
                if add_more != "y":
                    break  # Gives the user a quick exit back to the menu.

            save_guest_list()  # Persist once after the add session finishes.

        # -------------------- REMOVE NAMES -------------------- (Just to not get it complicated)
        # This checks if the user picked option 2 from the modify list.
        elif user_choice == "2":
            while True:  # Same as before, starts a loop that will keep running until the user stops.
                # Ask the user who she/he wants to remove
                name = input(
                    "Type a name that you want to remove (or type 'stop' to end): ")
                normalized_name = normalize(name)
                if normalized_name.lower() == "stop":
                    break  # Stops
                match = find_matching_name(normalized_name)
                if match:  # Case-insensitive removal of the stored name.
                    guest_list.remove(match)
                    # Then it lets the user know who he/she removed.
                    print("You removed:", match)
                else:  # This will only run if the user inputted was not found.
                    print("Name not found.")  # Displays and tell the user.

                # This then counts how many are in the guest_list.
                print("People now:", len(guest_list))
                # Displays and shows the latest updated list.
                print("Updated list:", guest_list)

                remove_more = input("Remove another? (y/n): ").strip().lower()
                if remove_more != "y":
                    break  # Allows quick exit instead of forcing 'stop'.

            save_guest_list()  # Persist removals once to limit file I/O.

        # -------------------- QUIT -------------------- (Just to not get it complicated)
        elif user_choice == "3":  # Checks once again if the user selects number 3.
            # Once the user selects number three it then displays this.
            print("Oke' goodbye :)")
            save_guest_list()  # Ensure final state is saved before leaving.
            break  # Then stop making it all end.
        else:
            # It displays if the user types other stuff other than in the modify list.
            print("Invalid choice, please choose from the given list numbers.")
except (EOFError, KeyboardInterrupt):
    print("\nSession ended unexpectedly; saving your list just in case...")
    save_guest_list()  # Added graceful shutdown with data persistence.
