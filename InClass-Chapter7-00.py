#Class Notes Chapter 7
# 11/06/2025

mylist = [2,3,4,5,6,7]
print(len(mylist))

print(8 in mylist)

thistuple = (1, 3, 7, 8, 7, 5, 4, 6)
tuple_to_list = list(thistuple)
print(tuple_to_list)

list_to_tuple = tuple(mylist)
print(list_to_tuple)

thislist = list(mylist)
print(thislist)

thislist = mylist.copy()
print(thislist)

import pandas as pd
import sklearn
import matplotlib.pyplot as plt
