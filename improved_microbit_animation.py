# Add your Python code here. E.g.
from microbit import *

star_bright = Image("90909:09990:99999:09990:90909")
star_dim = Image("50505:05550:55555:05550:50505")
empty = Image ("00000:00000:00000:00000:00000:")

stars = [empty, star_dim, star_bright, star_dim]

tree_bright = Image("00900:00900:09990:99999:05550")
tree_dim = Image("00500:00500:05950:59595:03330")

trees = [empty, tree_dim, tree_bright, tree_dim]

while True:
    if button_a.is_pressed():
        display.show(stars, delay=200)
        display.show(stars, delay=200)
    elif button_b.is_pressed():
        display.show(trees, delay=200)
        display.show(trees, delay=200)
    else:
        display.show(tree_dim)
