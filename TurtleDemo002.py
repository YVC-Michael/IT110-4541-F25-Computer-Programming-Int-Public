import turtle

#Named Constants
NUM_CIRCLES = 36 # Number of circles to draw
RADIUS = 100 # Radius of each circle
ANGLE = 10 # Angle to turn
COLORS = ['red', 'blue', 'green', 'yellow', 'purple', 'orange'] # List of colors to cycle through

#Loop
for x in range(NUM_CIRCLES):
    turtle.color(COLORS[x % len(COLORS)], COLORS[x % len(COLORS)])
    turtle.begin_fill()
    turtle.circle(RADIUS)
    turtle.end_fill()
    turtle.left(ANGLE)

# Keep window open
turtle.done()