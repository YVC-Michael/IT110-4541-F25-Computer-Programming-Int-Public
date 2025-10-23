### Look at the following function header:
### def my_function(a, b, c):
### Now look at the following call to my_function:
### my_function(3, 2, 1)
### When this call executes, what value will be assigned to a? What value will be assigned
### to b? What value will be assigned to c?

a = input("Enter a number: ")
b = input("Enter b number: ")
c = input("Enter c number: ")

def my_function(a, b, c):
    print(a, b, c)

my_function(a, b, c)
