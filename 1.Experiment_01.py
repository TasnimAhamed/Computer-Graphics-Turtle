import turtle

t = turtle.Turtle()
t.speed(3)

t.penup()
t.backward(250)
t.pendown()

def draw_star():
    for _ in range(5):
        t.forward(100)
        t.right(144)

for i in range(4):
    draw_star()
    t.penup()
    t.forward(150)
    t.pendown()

turtle.done()