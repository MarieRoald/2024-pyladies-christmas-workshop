import random
import turtle


def draw_line(
    x: int, y: int, xmax: int, ymax: int, scale: int, rng: random.Random
) -> None:
    if rng.choice([True, False]):
        turtle.penup()
        turtle.goto((x - xmax / 2) * scale, (y - ymax / 2) * scale)
        turtle.pendown()
        turtle.goto((x + 1 - xmax / 2) * scale, (y + 1 - ymax / 2) * scale)
    else:
        turtle.penup()
        turtle.goto((x + 1 - xmax / 2) * scale, (y - xmax / 2) * scale)
        turtle.pendown()
        turtle.goto((x - xmax / 2) * scale, (y + 1 - ymax / 2) * scale)


def draw_rectangle(x, y, w, h):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    for _ in range(2):
        turtle.forward(w)
        turtle.left(90)
        turtle.forward(h)
        turtle.left(90)


rng = random.Random(42)
turtle.pensize(3)
turtle.speed("fastest")
turtle.delay(0)

turtle.tracer(0)

xmax, ymax = 40, 40
scale = 20

turtle.setup(int(scale * xmax * 1.5), int(scale * ymax * 1.5))

turtle.color("#1e382f")

turtle.begin_fill()
draw_rectangle(
    -xmax * scale * 0.75, -ymax * scale * 0.75, xmax * scale * 1.5, ymax * scale * 1.5
)
turtle.end_fill()

turtle.color("#f9ddda")
for y in range(xmax):
    for x in range(ymax):
        draw_line(x, y, xmax, ymax, scale, rng)

turtle.hideturtle()

turtle.update()

turtle.getscreen().getcanvas().postscript(file="10print.eps")
turtle.done()
