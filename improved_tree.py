import turtle
t=turtle.Turtle()
t.color("darkgreen")

#  green triangles first
t.begin_fill()
points=[[0,150], [-40,100], [40,100], [0,150],
        [-10,100], [-50,50], [50,50], [10,100], [-10,100],
        [-10, 50], [-50, 0], [50,0], [10,50], [-10,50]]
# this is a for loop
for each in points:
  t.goto(each)
t.end_fill()

# then our box at the bottom
t.penup()
t.color("darkred")
t.begin_fill()
points=[ [15,0], [-15,0], [-15,-30], [15,-30],[15,0]]#first and last points are the same
for each in points:
  t.goto(each)
t.end_fill()

# now we can put baubles on the tree
points=[[-37,95], [37,95],
        [-46,45], [46,45], 
        [-50,-5], [50,-5]]
        
for each in points:
    t.goto(each)
    t.color("indigo")
    t.begin_fill()
    t.circle(5)
    t.end_fill()
    t.penup
    
    import turtle
# make a function called draw_star
def draw_star(size, color):
    angle = 130
    turtle.fillcolor(color)
    turtle.begin_fill()

    for side in range(5):
        turtle.forward(size)
        turtle.right(angle)
        turtle.forward(size)
        turtle.right(72 - angle)
    turtle.end_fill()
    return

# now draw the stars
turtle.penup()
turtle.goto(2,155)
turtle.pendown()
draw_star(10, "gold")
