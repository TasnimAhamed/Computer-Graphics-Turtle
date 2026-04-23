import turtle
t = turtle.Turtle()

screen = turtle.Screen()
root = screen._root

root.wm_attributes("-topmost", 1)

t.forward(100)

help(turtle)

turtle.done();