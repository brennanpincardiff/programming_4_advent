# Stars for the first day of Advent
import turtle
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

draw_star(70, "red")
draw_star(35, "green")

print("Happy 1st Day of Advent")
input()
