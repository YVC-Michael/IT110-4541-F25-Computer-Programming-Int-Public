###Areas of Rectangles

### The area of a rectangle is the rectangle’s length times its width. Write a program that asks
### for the length and width of two rectangles. The program should tell the user which rectangle
### has the greater area, or if the areas are the same.

print('Enter the length of the first rectangle: ')
rectangle_1_length = float(input())
print('Enter the width of the first rectangle: ')
rectangle_1_width = float(input())

print('Enter the length of the second rectangle: ')
rectangle_2_length = float(input())
print('Enter the width of the second rectangle: ')
rectangle_2_width = float(input())

rectangle_1_area = rectangle_1_length * rectangle_1_width
rectangle_2_area = rectangle_2_length * rectangle_2_width

if rectangle_1_area > rectangle_2_area:
    print(f'The first rectangle has the greater area: {rectangle_1_area:.2f}')
elif rectangle_1_area < rectangle_2_area:
    print(f'The second rectangle has the greater area: {rectangle_2_area:.2f}')
else:
    print(f'The areas of the two rectangle10s are equal: {rectangle_1_area:.2f}')
