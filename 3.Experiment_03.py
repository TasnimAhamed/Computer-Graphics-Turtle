import turtle

t = turtle.Turtle()
t.speed(0)

def dda(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    steps = max(abs(dx), abs(dy))

    x_inc = dx / steps
    y_inc = dy / steps

    x = x1
    y = y1

    for _ in range(int(steps)):
        t.penup()
        t.goto(round(x), round(y))
        t.pendown()
        t.dot(3)
        x += x_inc
        y += y_inc

# Example line
dda(-100, -50, 100, 80)

turtle.done()