import turtle
s=turtle.Screen()
t=turtle.Turtle()

#draw green trianges...
t.color("darkgreen")
t.begin_fill()
points=[[0,150], [-30,100], [30,100], [0,150],
        [0,100], [-45,50], [45,50], [0,100],
        [0, 50], [-50, 0], [50,0], [0,50]]

for each in points:
  t.goto(each)
t.end_fill()

#draw brown box for tree...
t.penup()
t.color("brown")
t.begin_fill()
points=[[15,0], [-15,0], [-15,-15], [15,-15],[15,0]]#first and last points are the same
for each in points:
  t.goto(each)
t.end_fill()


#draw red circles...
points=[[-30,95], [30,95],
        [-45, 45], [45,45],
        [-50, -5], [50, -5]]

for each in points:
    t.goto(each)
    t.color("red")
    t.begin_fill()
    t.circle(5)
    t.end_fill()
    t.penup()

turtle.exitonclick()
