import turtle

t = turtle.Turtle()
t.speed(0)

def bresenham(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    x, y = x1, y1

    sx = 1 if x2 > x1 else -1
    sy = 1 if y2 > y1 else -1

    if dy <= dx:
        p = 2 * dy - dx
        for _ in range(dx):
            t.penup()
            t.goto(x, y)
            t.pendown()
            t.dot(3)

            x += sx
            if p < 0:
                p += 2 * dy
            else:
                y += sy
                p += 2 * (dy - dx)
    else:
        p = 2 * dx - dy
        for _ in range(dy):
            t.penup()
            t.goto(x, y)
            t.pendown()
            t.dot(3)

            y += sy
            if p < 0:
                p += 2 * dx
            else:
                x += sx
                p += 2 * (dx - dy)


bresenham(-100, -50, 120, 80)

turtle.done()