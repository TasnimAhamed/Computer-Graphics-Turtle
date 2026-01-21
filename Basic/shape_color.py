import turtle

t = turtle.Turtle()

# Screen on Top
screen = turtle.Screen()
root = screen._root
root.wm_attributes("-topmost", 1)

# Shape change
t.shape("turtle")
t.color("red", "yellow")
pen , fill = t.color() # ["Black", "Black"] => Pen color and Fill Color
# print(pen)
# print(fill)

t.forward(100)

turtle.done()
