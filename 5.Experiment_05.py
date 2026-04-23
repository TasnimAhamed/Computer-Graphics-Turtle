import turtle

t = turtle.Turtle()
t.speed(0)

def draw_points(xc, yc, x, y):
    points = [
        (xc + x, yc + y), (xc - x, yc + y),
        (xc + x, yc - y), (xc - x, yc - y),
        (xc + y, yc + x), (xc - y, yc + x),
        (xc + y, yc - x), (xc - y, yc - x)
    ]
    for px, py in points:
        t.penup()
        t.goto(px, py)
        t.pendown()
        t.dot(3)

def midpoint_circle(xc, yc, r):
    x = 0
    y = r
    p = 1 - r   # decision parameter

    draw_points(xc, yc, x, y)

    while x < y:
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1

        draw_points(xc, yc, x, y)


midpoint_circle(0, 0, 100)

turtle.done()