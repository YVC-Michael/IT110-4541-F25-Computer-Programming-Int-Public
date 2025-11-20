#Class Notes Chapter 8
# 11/13/2025

#String Indexing
my_string = 'Roses are red'
print(len(my_string)-1)
print(my_string[0])
print(my_string[-1])

#Concatenation
my_string1 = 'Roses are red'
my_string2 = 'Violets are blue'
print(my_string1 + my_string2)
print(my_string1 + ' ' + my_string2)
#string3 = string1 += string2
#print(string3)

my_name = 'Carmen'
my_name = my_name + ' Brown'
print(my_name)

#String Slicing
my_string = 'Roses are red'
print(my_string[0:5])
print(my_string[1:7])

#Password Match
password = 'password123'
password2 = 'password123'
if password not in password2:
    print('Password not match')
else:
    print('Password match')

if password in password2:
    print('Password match')
else:
    print('Password do not match')

#String Methods    
print(password.isalnum())
print(password.isalpha())
print(password.isdigit())
print(password.islower())
print(password.isupper())
print(password.lower())
print(password.upper())

#String Strip
my_left_strip = '\n \t Roses are red'
my_right_strip = 'Roses are red\n \t'
my_strip = '\n \t Roses are red\n \t'

print(my_strip.strip('red'))
print(my_left_strip.lstrip())
print(my_right_strip.rstrip())

#String Find
find_me = 'Roses are red'
print(find_me.find('are'))
print(find_me.index('are'))
print(find_me.count('are'))
print(find_me.replace('are', 'blue'))
print(find_me.split(' '))

#Repetition Operator
my_repeat = 'Roses are red '
print(my_repeat * 3)

#Splitting a String
my_split = 'Roses are red/Roses are blue/Roses are green'
print(my_split.split('/'))
my_tuple = tuple(my_split.split('/'))
print(my_tuple)

#String Tokens
str_token = 'peach rasberry strawberry vanilla'
my_token = str_token.split(' ')

mySchool = "YVC Campus"

print(mySchool)
print (mySchool.lstrip())

if mySchool.startswith('Y'):
    print('The word', mySchool, 'starts with Y')
else:
    print('The word', mySchool, 'does not start with Y')

if mySchool.endswith('s'):
    print('The word', mySchool, 'ends with s')
else:
    print('The word', mySchool, 'does not end with s')

print('When I use "*" to repeat my school name 5x, I get.')
print(mySchool * 5)

mySchool = mySchool.replace('YVC Campus', 'Grandview Campus')

print(f'My other school is {mySchool}')

hisFname = 'Michael'

#charSearched = input('Enter a character to search for: ')
#CharInName = hisFname.count(charSearched)

myName = 'Neanderthal'
charCount = 0
print(f'There are {len(myName)} characters in {myName}')
for eachLetter in myName:
    print(f'The character in postion {charCount+1} is {eachLetter}')
    charCount += 1

#String Formatting
my_format = 'this is a sentance'
print('Capitalized:\t', my_format.capitalize())
print('Lowercase:\t', my_format.lower())
print('Uppercase:\t', my_format.upper())
print('Title:\t\t', my_format.title())
print('Swapcase:\t', my_format.swapcase())
print('Strip:\t\t', my_format.strip())
print('Left Strip:\t', my_format.lstrip())
print('Right Strip:\t', my_format.rstrip())
print('Center:\t\t', my_format.center(30))
print('Left Justify:', my_format.ljust(30))
print('Right Justify:', my_format.rjust(30))
print('Zfill:\t\t', my_format.zfill(30))
