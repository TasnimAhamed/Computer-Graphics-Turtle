import turtle

screen = turtle.Screen()
screen._root.attributes("-topmost", True)

t = turtle.Turtle()
t.shape("turtle")

t.color("red")
for i in range(5):
    t.speed(i)
    t.forward(150)
    t.right(144)

turtle.done()
