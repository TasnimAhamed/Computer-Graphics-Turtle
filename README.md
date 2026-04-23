
## 🎨 Computer Graphics Lab Experiments

---

### Experiment 01: Draw 4 Stars
**Description:** Implementation of a program to draw 4 stars using Turtle graphics.

**Solution:**
```python
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
```

---

### Experiment 02: Draw 8×8 Chess Board
**Description:** Create an 8×8 chess board pattern with alternating colors.

**Solution:**
```python
import turtle

t = turtle.Turtle()
t.speed(0)

square_size = 80


def draw_square(color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(4):
        t.forward(square_size)
        t.right(90)
    t.end_fill()


t.penup()
t.goto(-160, 160)
t.pendown()

colors = ["black", "white"]

for row in range(8):
    for col in range(8):
        draw_square(colors[(row + col) % 2])
        t.forward(square_size)

    t.backward(square_size * 8)
    t.right(90)
    t.forward(square_size)
    t.left(90)

turtle.done()
```

---

### Experiment 03: Implementation of DDA Line Algorithm
**Description:** Implement the Digital Differential Analyzer (DDA) line drawing algorithm.

**Solution:**
```python
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
```

---

### Experiment 04: Implementation of Bresenham Line Algorithm
**Description:** Implement Bresenham's line drawing algorithm for efficient line rendering.

**Solution:**
```python
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
```

---

### Experiment 05: Implementation of Midpoint Circle Drawing Algorithm
**Description:** Implement the Midpoint Circle algorithm for drawing circles efficiently.

**Solution:**
```python
# Solution will be added here
```

---

### Experiment 06: Draw a Flag of Bangladesh using Circle Algorithm
**Description:** Create the flag of Bangladesh using circle drawing algorithms.

**Solution:**
```python
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
```

---

### Experiment 07: Draw Shaheed Minar of Bangladesh using Midpoint Circle Algorithm
**Description:** Draw the iconic Shaheed Minar monument using the Midpoint Circle algorithm.

**Solution:**
```python
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
```

---

### Experiment 08: Draw Bicycle Using OpenGL
**Description:** Create a bicycle illustration using OpenGL graphics library.

**Solution:**
```python
# Solution will be added here
```

---

### Experiment 09: Implementation of 2D Transformation
**Description:** Implement 2D geometric transformations including:
- Translation
- Scaling
- Rotation
- Reflection
- Shearing

**Solution:**
```python
# Solution will be added here
```

---

### Experiment 10: Implementation of 3D Transformation
**Description:** Implement 3D geometric transformations including:
- Translation
- Scaling
- Rotation
- Reflection
- Shearing

**Solution:**
```python
# Solution will be added here
```

---

## 👨‍💻 Author

*Mohammad Tasnim Ahmed*

---

## 📄 License

This project is created for educational purposes as part of the Computer Graphics course.

---