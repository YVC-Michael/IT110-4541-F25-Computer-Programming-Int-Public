###Wi-Fi Diagnostic Tree

### Figure 3-19 shows a simplified flowchart for troubleshooting a bad Wi-Fi connection. Use
### the flowchart to create a program that leads a person through the steps of fixing a bad
### Wi-Fi connection. Here is an example of the program’s output:
### Reboot the computer and try to connect.
### Did that fix the problem? no [Enter]
### Reboot the router and try to connect.
### Did that fix the problem? yes [Enter]
### Notice the program ends as soon as a solution is found to the problem. Here is another
### example of the program’s output:
### Reboot the computer and try to connect.
### Did that fix the problem? no [Enter]
### Reboot the router and try to connect.
### Did that fix the problem? no [Enter]
### Make sure the cables between the router and modem are plugged in firmly.
### Did that fix the problem? no [Enter]
### Move the router to a new location.
### Did that fix the problem? no [Enter]
### Get a new router.

#Flag Variable
router_fixed = False

#Output
print('\nI hear that you are having trouble connecting to Wi-Fi. My diagnostic tool will'
    '\nlead you through a series of steps to identify and resolve the problem.'
    '\n\n')

#Computer Reboot
print('Reboot the computer and try to connect.')
user_input = input('\nDid that fix the problem? (yes/no): ')
if user_input == 'yes':
    print('\nYour Wi-Fi connection is working.')
    router_fixed = True
else:
    print('\nReboot the router and try to connect.')

#Router Reboot
if router_fixed == False:
    user_input = input('\nDid that fix the problem? (yes/no): ')
    if user_input == 'yes':
        print('\nYour Wi-Fi connection is working.')
        router_fixed = True
    else:
        print('\nMake sure the cables between the router & modem are plugged in firmly.')

#Cable Check
if router_fixed == False:
    user_input = input('\nDid that fix the problem? (yes/no): ')
    if user_input == 'yes':
        print('\nYour Wi-Fi connection is working.')
        router_fixed = True
    else:
        print('\nMove the router to a new location and try to connect.')

#Move Router
if router_fixed == False:
    user_input = input('\nDid that fix the problem? (yes/no): ')
    if user_input == 'yes':
        print('\nYour Wi-Fi connection is working.')
        router_fixed = True
    else:
        print('\nGet a new router.')
