import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.tracer(0)
t.speed(0)
t.hideturtle()

# Flag dimensions
H = 300
W = (10/6) * H

# Circle properties
r = H / 5
cx = -W/2 + (W * 2/5)
cy = 0

# Draw green rectangle (flag)
t.penup()
t.goto(-W/2, H/2)
t.pendown()
t.color("green")
t.begin_fill()
for _ in range(2):
    t.forward(W)
    t.right(90)
    t.forward(H)
    t.right(90)
t.end_fill()

# Midpoint Circle Algorithm
def draw_points(xc, yc, x, y):
    points = [
        (xc + x, yc + y), (xc - x, yc + y),
        (xc + x, yc - y), (xc - x, yc - y),
        (xc + y, yc + x), (xc - y, yc + x),
        (xc + y, yc - x), (xc - y, yc - x)
    ]
    t.color("red")
    for px, py in points:
        t.goto(px, py)
        t.pendown()
        t.dot(3, "red")

def midpoint_circle(xc, yc, r):
    x = 0
    y = int(r)
    p = 1 - r

    draw_points(xc, yc, x, y)

    while x < y:
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1

        draw_points(xc, yc, x, y)

t.penup()
midpoint_circle(cx, cy, r)


# Bamboo pole
pole_x = -W/2
t.penup()
t.goto(pole_x, H/2)
t.setheading(-90)
t.pendown()

t.color("#8B5A2B")
t.begin_fill()

for _ in range(2):
    t.forward(H*2)
    t.right(90)
    t.forward(15)   # pole width
    t.right(90)

t.end_fill()


turtle.done()