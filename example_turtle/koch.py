import turtle


def snowflake_side(length, order):
    if order > 0:
        snowflake_side(length / 3, order - 1)
        turtle.left(60)
        snowflake_side(length / 3, order - 1)
        turtle.right(120)
        snowflake_side(length / 3, order - 1)
        turtle.left(60)
        snowflake_side(length / 3, order - 1)
    else:
        turtle.forward(length)


# Draw the snowflake
turtle.speed("fastest")

for side in range(6):
    snowflake_side(100, 3)
    turtle.right(300)
turtle.done()
