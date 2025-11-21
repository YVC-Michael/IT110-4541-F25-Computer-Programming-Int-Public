from pathlib import Path  # Added to build a save path relative to this file.

DEFAULT_GUEST_LIST = [  # Stored separately so we can reuse it when the file is missing.
    "Chidi", "Lucas", "Miriam", "Jorge",
    "Gwen", "Nneka", "Egan", "Estella", "Josh"
]

GUEST_FILE = Path(__file__).with_name("guest_list.txt")  # Keeps saves next to the script.


def load_guest_list():
    """Import names from guest_list.txt when it already exists."""
    # Unlike the original script, we bring forward any previously saved guests before using defaults.
    if GUEST_FILE.exists():
        with GUEST_FILE.open("r", encoding="utf-8") as file:
            loaded_names = [line.strip().title() for line in file if line.strip()]
        if loaded_names:
            print(f"Loaded {len(loaded_names)} guests from existing file.")
            return loaded_names
    print("Starting with the default guest list provided in the project scenario.")
    return DEFAULT_GUEST_LIST.copy()  # Use copy so the constant never mutates directly.


# 1.I first start with the guest list given that was given in the scenario.
guest_list = load_guest_list()  # Original script always started with the hardcoded list.


def save_guest_list():
    """Persist the guest list to disk once per add/remove session."""
    with GUEST_FILE.open("w", encoding="utf-8") as file:
        for name in guest_list:
            file.write(name + "\n")
    print(f"\nList saved to file: {GUEST_FILE}")  # Added spacing to separate from prior output.


def normalize(name_input):
    """Clean up user input and prevent blank additions."""
    # Added whitespace stripping to keep inputs clean, which the original version lacked.
    return name_input.strip()


def find_matching_name(candidate):
    """Locate an existing name ignoring case so remove/add checks are consistent."""
    # This helper enables case-insensitive comparisons instead of the direct == checks in the baseline code.
    candidate_lower = candidate.lower()
    for stored in guest_list:
        if stored.lower() == candidate_lower:
            return stored
    return None


def display_guest_list(context_label):
    """Show the names in three evenly spaced columns for easier reading."""
    # The original script printed the raw list; this helper formats names in neat columns.
    if not guest_list:
        print(f"{context_label}: (no guests yet)")
        return

    column_width = max(len(name) for name in guest_list) + 4  # Keeps spacing consistent.
    columns = 3
    print(f"{context_label}:")
    for start in range(0, len(guest_list), columns):
        chunk = guest_list[start:start + columns]
        formatted_row = "".join(name.ljust(column_width) for name in chunk)
        print(f"    {formatted_row.rstrip()}")


try:
    print("Welcome to the Emil Kissel Park Cookout List Updater!")  # Explains the purpose upfront.
    print("Use this tool to add or remove guests and keep the roster saved to file.\n")
    # Intro text above is new to orient users before presenting the menu loop.
    # 2.Second, I use the while loop to make it loop the menu forever until user stops.
    display_guest_list("Current guest list")  # Show the starting roster before prompting.
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
            # Enhancement: allow multiple adds per entry and guide users with stop/y prompts.
            while True:
                name = input(
                    "\nType the first name that you want to add (or type 'stop' to end): ")
                normalized_name = normalize(name)  # Removes extra spaces before storing.
                if normalized_name.lower() == "stop":
                    break  # Stops
                if not normalized_name:
                    print("Please enter a non-empty name.")  # Prevents blank entries.
                    continue
                formatted_name = normalized_name.title()  # Force Title Case regardless of user input.
                if find_matching_name(formatted_name):
                    print("\nThat name is already on the list.")  # Avoid duplicate entries.
                    continue
                # If the user types a given name, then that name will be placed at the last of the guest list.
                guest_list.append(formatted_name)
                print(f"\nYou added: {formatted_name}")  # Added leading newline to highlight the event.
                # This lets the program count how many are in the list.
                print(f"\nThe list now has {len(guest_list)} people.")
                # This just prints the guest_list with the current updated one.
                display_guest_list("\nUpdated list")  # Cleaner output than the raw list repr.

                add_more = input("\nAdd another? (y/n): ").strip().lower()
                if add_more != "y":
                    break  # Gives the user a quick exit back to the menu.

            save_guest_list()  # Persist once after the add session finishes.

        # -------------------- REMOVE NAMES -------------------- (Just to not get it complicated)
        # This checks if the user picked option 2 from the modify list.
        elif user_choice == "2":
            # Enhancement: show the list before removing so users have context.
            display_guest_list("\nCurrent guest list")  # Show the roster so users know what's available to remove.
            while True:  # Same as before, starts a loop that will keep running until the user stops.
                # Ask the user who she/he wants to remove
                name = input(
                    "\nType a name that you want to remove (or type 'stop' to end): ")
                normalized_name = normalize(name)
                if normalized_name.lower() == "stop":
                    break  # Stops
                match = find_matching_name(normalized_name)
                if match:  # Case-insensitive removal of the stored name.
                    guest_list.remove(match)
                    # Then it lets the user know who he/she removed.
                    print(f"\nYou removed: {match}")
                else:  # This will only run if the user inputted was not found.
                    print("Name not found.")  # Displays and tell the user.

                # This then counts how many are in the guest_list.
                print(f"\nThe list now has {len(guest_list)} people.\n")
                # Displays and shows the latest updated list.
                display_guest_list("Updated list")  # Cleaner output than the raw list repr.

                remove_more = input("\nRemove another? (y/n): ").strip().lower()
                if remove_more != "y":
                    break  # Allows quick exit instead of forcing 'stop'.

            save_guest_list()  # Persist removals once to limit file I/O.

        # -------------------- QUIT -------------------- (Just to not get it complicated)
        elif user_choice == "3":  # Checks once again if the user selects number 3.
            # Once the user selects number three it then displays this.
            print("\nOke' goodbye :)")
            save_guest_list()  # Ensure final state is saved before leaving.
            break  # Then stop making it all end.
        else:
            # It displays if the user types other stuff other than in the modify list.
            print("Invalid choice, please choose from the given list numbers.")
except (EOFError, KeyboardInterrupt):
    print("\nSession ended unexpectedly; saving your list just in case...")
    save_guest_list()  # Added graceful shutdown with data persistence.
