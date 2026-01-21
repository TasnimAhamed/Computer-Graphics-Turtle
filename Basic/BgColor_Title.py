import turtle

t = turtle.Turtle()

screen = turtle.Screen()
root = screen._root
root.wm_attributes("-topmost", 1)

# Title
screen.title("Background Color and Title")

# Shape
t.shape("turtle")

# pen and fill color
t.color("white", "white")

# Background Color
screen.bgcolor("black")

# set Background Pic
#screen.bgpic("background.gif") # bg must be gif

# Square
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.left(45)
t.color("red", "white")
t.forward(141.25)

turtle.done()

