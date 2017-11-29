import turtle
s=turtle.Screen()
t=turtle.Turtle()
t.color("darkgreen")
#one way to draw a tree
t.begin_fill()
points=[[0,150], [-30,100], [30,100], [0,150],
        [0,100], [-45,50], [45,50], [0,100],
        [0, 50], [-50, 0], [50,0], [0,50]]

for each in points:
  t.goto(each)
t.end_fill()

t.penup()
t.color("brown")
t.begin_fill()
points=[ [15,0], [-15,0], [-15,-15], [15,-15],[15,0]]#first and last points are the same
for each in points:
  t.goto(each)
t.end_fill()


input()
