import turtle
t=turtle.Turtle()
t.color("darkgreen")

#  green triangles first
t.begin_fill()
points=[[0,150], [-30,100], [30,100], [0,150],
        [0,100], [-45,50], [45,50], [0,100],
        [0, 50], [-50, 0], [50,0], [0,50]]
# this is a for loop
for each in points:
  t.goto(each)
t.end_fill()

# then our box at the bottom
t.penup()
t.color("brown")
t.begin_fill()
points=[ [15,0], [-15,0], [-15,-15], [15,-15],[15,0]]#first and last points are the same
for each in points:
  t.goto(each)
t.end_fill()

# could you put yesterday's star on the top?
turtle.exitonclick()

