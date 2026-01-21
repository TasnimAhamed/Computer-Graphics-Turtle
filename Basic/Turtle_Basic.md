# 🐢 Learning Python Turtle for Computer Graphics

## 1️⃣ Introduction to Turtle Graphics

Turtle Graphics is a Python library used to introduce students to:

- Basic computer graphics concepts
- Coordinate geometry
- Line and circle drawing algorithms

The turtle behaves like a pen that moves on a Cartesian plane and draws as it moves.

## 2️⃣ Basic Setup & First Program

```python
import turtle

t = turtle.Turtle()
t.forward(100)
turtle.done()
```

### Key Concepts

- **Default position:** (0, 0)
- **Default direction:** Right (East)
- **Drawing happens while the pen is down**

## 3️⃣ Core Turtle Functions (Must Learn)

### 🟢 Movement Functions

```python
t.forward(distance)
t.backward(distance)
t.left(angle)
t.right(angle)
```

### 🟢 Position Control

```python
t.goto(x, y)
t.setx(x)
t.sety(y)
t.home()
```

### 🟢 Pen Control

```python
t.penup()
t.pendown()
t.pensize(3)
```

### 🟢 Color & Fill

```python
t.color("red")
t.fillcolor("green")
t.begin_fill()
t.end_fill()
```

### 🟢 Speed & Visibility

```python
t.speed(5)
t.hideturtle()
t.showturtle()
```

## 4️⃣ Drawing Basic Shapes

### Example: Square

```python
for _ in range(4):
    t.forward(100)
    t.left(90)
```

### Example: Circle

```python
t.circle(50)
```

## 5️⃣ Understanding Coordinates & Screen

```python
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Turtle Graphics")
```

- **Origin:** (0, 0)
- **X-axis** → horizontal
- **Y-axis** → vertical

## 6️⃣ Digital Differential Analyzer (DDA) Line Algorithm

### 📌 Description

DDA is a line drawing algorithm that calculates intermediate points between two endpoints using incremental steps.

### 📐 Algorithm Steps

1. Calculate dx and dy
2. Determine the number of steps
3. Increment x and y accordingly
4. Plot each point

### 🧪 Sample Implementation (Turtle)

```python
def dda(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    steps = max(abs(dx), abs(dy))
    x_inc = dx / steps
    y_inc = dy / steps

    x, y = x1, y1
    t.penup()
    t.goto(x, y)
    t.pendown()

    for _ in range(steps):
        t.goto(round(x), round(y))
        x += x_inc
        y += y_inc
```

## 7️⃣ Bresenham's Line Drawing Algorithm

### 📌 Description

Bresenham's algorithm draws lines using integer calculations, making it faster and more efficient than DDA.

### 📐 Algorithm Features

- Uses decision parameter
- Avoids floating-point arithmetic
- Efficient for raster displays

### 🧪 Sample Implementation (Turtle)

```python
def bresenham(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    x, y = x1, y1
    sx = 1 if x2 > x1 else -1
    sy = 1 if y2 > y1 else -1

    if dx > dy:
        p = 2 * dy - dx
        for _ in range(dx):
            t.goto(x, y)
            x += sx
            if p < 0:
                p += 2 * dy
            else:
                y += sy
                p += 2 * (dy - dx)
    else:
        p = 2 * dx - dy
        for _ in range(dy):
            t.goto(x, y)
            y += sy
            if p < 0:
                p += 2 * dx
            else:
                x += sx
                p += 2 * (dx - dy)
```

## 8️⃣ Midpoint Circle Drawing Algorithm

### 📌 Description

The Midpoint Circle algorithm draws a circle by calculating points using symmetry and decision parameters.

### 📐 Algorithm Features

- Uses 8-way symmetry
- Efficient integer arithmetic

### 🧪 Sample Implementation (Turtle)

```python
def draw_circle(xc, yc, r):
    x = 0
    y = r
    p = 1 - r

    def plot(x, y):
        points = [
            (xc + x, yc + y), (xc - x, yc + y),
            (xc + x, yc - y), (xc - x, yc - y),
            (xc + y, yc + x), (xc - y, yc + x),
            (xc + y, yc - x), (xc - y, yc - x)
        ]
        for px, py in points:
            t.goto(px, py)

    while x <= y:
        plot(x, y)
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1
```

## 9️⃣ Drawing the Flag of Bangladesh

### 📌 Description

The national flag consists of:

- Green rectangular background
- Red circle slightly shifted toward the hoist

### 🧪 Sample Implementation

```python
# Green background
t.penup()
t.goto(-200, 100)
t.pendown()
t.color("green")
t.begin_fill()
for _ in range(2):
    t.forward(400)
    t.right(90)
    t.forward(200)
    t.right(90)
t.end_fill()

# Red circle
t.penup()
t.goto(0, -20)
t.color("red")
t.begin_fill()
t.circle(50)
t.end_fill()
```
---

**Happy Learning! 🚀**