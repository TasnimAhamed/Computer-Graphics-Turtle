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