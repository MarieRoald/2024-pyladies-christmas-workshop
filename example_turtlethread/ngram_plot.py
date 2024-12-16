import math
import turtlethread

from dhlab.ngram.nb_ngram import nb_ngram


def draw_tick(tick_width, turtle: turtlethread.Turtle):
    turtle.right(90)
    turtle.forward(tick_width)
    turtle.backward(2 * tick_width)
    turtle.forward(tick_width)
    turtle.left(90)


def draw_arrow_head(tick_width: float, turtle: turtlethread.Turtle):
    L = math.sqrt(2) * tick_width
    turtle.right(45)
    turtle.backward(L)
    turtle.forward(L)
    turtle.left(90)
    turtle.backward(L)
    turtle.forward(L)
    turtle.right(45)


def draw_axis(
    axis_length: float,
    ticks: list[float],
    tick_width: float,
    turtle: turtlethread.Turtle,
):
    ticks = sorted(ticks)
    if ticks and axis_length < ticks[-1]:
        raise ValueError("Axis length must be greater than the largest tick value")

    offset = 0
    for i, tick in enumerate(ticks):
        if i > 0:
            draw_tick(tick_width, turtle)

        turtle.forward(tick - offset)
        offset = tick

    if ticks:
        draw_tick(tick_width, turtle)
    turtle.forward(axis_length - offset)

    draw_arrow_head(tick_width, turtle)
    turtle.backward(axis_length + tick_width)
    turtle.forward(tick_width)


if __name__ == "__main__":
    # Get the word frequency data
    year_min, year_max = 1860, 2020
    ngram = nb_ngram("jul", corpus="avis", smooth=1, years=(year_min, year_max))
    ngram /= ngram.max()

    # Parametrize the axes
    xmax = 750
    ymax = 500
    x_values = [xmax * (year - year_min) / (year_max - year_min) for year in ngram.index]
    y_values = [freq * ymax for freq in ngram["jul"]]
    tick_distance = math.floor(20 * xmax / (year_max - year_min))  # Tick every 20th year

    # Create the turtle object
    turtle = turtlethread.Turtle()

    # Draw the x- and y-axis, adding ticks on the x-axis only
    with turtle.triple_stitch(30):
        draw_axis(xmax + tick_distance, range(0, xmax, tick_distance), 10, turtle)
        turtle.left(90)
        draw_axis(ymax, [], 10, turtle)

    # Move the the starting position of the line-plot
    with turtle.jump_stitch():
        turtle.goto(x_values[0], y_values[0])

    # Draw the frequency line
    with turtle.running_stitch(30):
        for x, y in zip(x_values, y_values):
            turtle.goto(x, y)

    # Save the pattern
    turtle.save("plot.png")
    turtle.show_info()
    turtle.save("plot.jef")
