import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.setup(width=900, height=600)
screen.tracer(0)
t.speed(0)
t.hideturtle()
t.pensize(2)

# Rectangle with border
def draw_rect(x, y, w, h, fill_color):
    t.penup()
    t.goto(x, y)
    t.setheading(0)   # 🔥 FIX: reset direction every time
    t.pendown()

    t.color("black", fill_color)
    t.begin_fill()

    for _ in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)

    t.end_fill()
    t.penup()   # 🔥 keep turtle state clean after each shape


# BASE
draw_rect(-300, -220, 600, 70, "#7f7f7f")

# STAIRS (3 layers)
draw_rect(-250, -150, 500, 30, "#bfbfbf")
draw_rect(-200, -120, 400, 25, "#d9d9d9")
draw_rect(-150, -95, 300, 20, "#efefef")



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
midpoint_circle(0, 150, 100)


# CENTER PILLAR
draw_rect(-15, -95, 30, 260, "white")

# 2nd pillars
draw_rect(-80, -95, 25, 200, "white")
draw_rect(55, -95, 25, 200, "white")

# 3rd pillars
draw_rect(-140, -95, 20, 150, "white")
draw_rect(120, -95, 20, 150, "white")

# 4th pillars (small)
draw_rect(-190, -95, 15, 110, "white")
draw_rect(175, -95, 15, 110, "white")


screen.update()
turtle.done()