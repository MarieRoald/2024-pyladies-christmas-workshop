import turtle
import random

def draw_rectangle(x, y, w, h, turtle):
    """We use this function to draw the background
    """
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    for _ in range(2):
        turtle.forward(w)
        turtle.left(90)
        turtle.forward(h)
        turtle.left(90)
    turtle.goto(x, y)  # Because of roundoff errors


# Parametrize the drawing
row = 0
num_petals = 11
num_columns = 11
num_rows = 10
petal_size = 12.5
grid_size = 4 * petal_size
padding = 0.5
random.seed(42)

star_colors = ["#f6b36c", "#ffffff", "#85aaf0"]

# Setup Turtle
pen = turtle.Turtle()
pen.speed("fastest")
turtle.tracer(0)
turtle.setup(num_columns*grid_size * (1 + padding), num_rows*grid_size * (1 + padding))

# Draw the background
pen.color("#14174c")
pen.begin_fill()
draw_rectangle(
    -num_columns * grid_size * (1 + padding)/2,
    -num_rows * grid_size * (1 + padding)/2,
    num_columns * grid_size * (1 + padding),
    num_rows*grid_size * (1 + padding),
    pen
)
pen.end_fill()


# Draw the starscape
for row in range(num_rows):
    s = row / num_rows
    for column in range(num_columns):
        
        pen.penup()
        dx = random.gauss(0, s/2)
        dy = random.gauss(0, s/2)

        # Subtract 0.5 to have the flowers centered on the grid
        pen.goto((num_columns/2 - column - 0.5 + dx) * grid_size, (num_rows / 2 - row - 0.5 + dy) * grid_size)
        pen.pendown()

        # Randomly select a colour and draw a star
        pen.color(random.choice(star_colors))
        for petal in range(num_petals):
            petal_size = abs(random.gauss(15, 5*s))
            for side in range(4):
                pen.forward(petal_size)
                pen.right(90)
            pen.right(360 / num_petals)

# Save the figure
pen.hideturtle()
turtle.update()
turtle.getscreen().getcanvas().postscript(file="starscape.eps")
turtle.done()
