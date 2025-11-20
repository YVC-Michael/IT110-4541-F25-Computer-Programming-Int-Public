### Look at the following function definition:
### def my_function(a, b, c):
###     d = (a + c) / b
###     print(d)

### a. Write a statement that calls this function and uses keyword arguments to pass 2
### into a, 4 into b, and 6 into c.
### my_function(a=2, b=4, c=6)

### b. What value will be displayed when the function call executes?
### The value displayed will be 2.0

a = int(input("Enter 2: "))
b = int(input("Enter 4: "))
c = int(input("Enter 6: "))

def my_function(a, b, c):
     global d
     d = (a + c) / b
     return(d)

my_function(a, b, c)
print()
print(d)
print()
