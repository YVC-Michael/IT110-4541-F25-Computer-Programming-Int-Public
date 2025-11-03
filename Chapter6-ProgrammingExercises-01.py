###1. File Display

### Assume a file containing a series of integers is named numbers.txt and exists on the com-
### puter’s disk. Write a program that displays all of the numbers in the file.

def import_file():
    file = open("./Files/numbers.txt")
    for line in file:
        print(int(line))
    file.close()

# Call function
import_file()
