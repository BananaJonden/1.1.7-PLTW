#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]  
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  t.penup()
  my_turtles.append(t)
  t.color(turtle_colors[len(turtle_colors) - 1])
  turtle_colors.pop()

# creates 2 variables that change the value of the x and y coordinates of the set-positions
startx = 0
starty = 0
direction = 90
# Goes back to begining and creates the line for the first section
for t in my_turtles:
  t.goto(startx, starty)
  t.pendown()
  t.setheading(direction)
  t.right(45)     
  direction = t.heading()
  
  t.forward(50)
  t.pendown()
  startx = t.xcor()
  starty = t.ycor()

wn = trtl.Screen()
wn.mainloop() 