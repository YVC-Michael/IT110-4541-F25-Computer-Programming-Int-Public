### Write an if statement that uses the turtle graphics library to determine whether the
### turtle is inside of a rectangle. The rectangle’s upper-left corner is at (100, 100) and its
### lower-right corner is at (200, 200). If the turtle is inside the rectangle, hide the turtle.

import turtle

turtle.penup()
turtle.goto(100, 100)
turtle.pendown()
turtle.goto(100, 200)
turtle.goto(200, 200)
turtle.goto(200, 100)
turtle.goto(100, 100)

turtle_user_x = int(input('Give me an x coordinate: '))
turtle_user_y = int(input('Give me a y coordinate: '))

turtle.hideturtle()
turtle.penup()
turtle.goto(0, 0)
turtle.showturtle()
turtle.pendown()

if turtle_user_x >= 100 and turtle_user_x <= 200 and turtle_user_y >= 100 and turtle_user_y <= 200:
    turtle.goto(turtle_user_x, turtle_user_y)
    turtle.hideturtle()
    turtle.done()
else:
    turtle.goto(turtle_user_x, turtle_user_y)
    turtle.done()
