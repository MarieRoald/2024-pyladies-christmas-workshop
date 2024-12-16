import turtle
import random

turtle.tracer(0)  # Disable live drawing
num_squares = 10
num_rows = 10
num_columns = 3

for x in range(num_columns):
    s = x / (num_columns - 1)
    for y in range(num_rows):
        turtle.penup()
        dx, dy = random.gauss(0, 50 * s), random.gauss(0, 50 * s)
        turtle.goto((num_columns / 2 - x) * 100, (num_rows / 2 - y) * 100)
        turtle.pendown()

        for square in range(num_squares):
            for side in range(4):
                turtle.forward(30)
                turtle.right(90)
            turtle.right(360 / num_squares)

turtle.update()  # Draw every command so far at once
turtle.done()
