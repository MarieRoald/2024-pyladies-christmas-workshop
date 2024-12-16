# Inspired by https://medium.com/@limkao/teach-you-to-draw-a-christmas-tree-in-python-80f4bcf8c9d5

import turtle


def draw_branch(d, s):
    """Each branch consists of two "side-branches" and a "main branch".

    Once a branch is drawn, the turtle is at the same place as it started
    """
    if d <= 0:
        return

    # Move a little bit forwards before drawing the side branches
    turtle.forward(s)

    # Draw the right branch. The turtle is where it started after these two lines
    turtle.right(120)
    draw_branch(d - 3, s * 0.5)

    # Draw the left branch. The turtle is where it started after these two lines
    turtle.right(120)
    draw_branch(d - 3, s * 0.5)

    # Rotate back to the initial heading
    turtle.right(120)

    # Draw the main branch. The turtle is where it started after this line
    draw_branch(d - 1, s * 0.8)

    # Move back to where the turtle started
    turtle.backward(s)


n = 100

turtle.speed("fastest")  # set speed

turtle.left(90)
turtle.penup()
turtle.backward(400)
turtle.pendown()

turtle.color("dark green")

# The christmas tree is drawn as one large branch
draw_branch(11, n)
turtle.backward(n / 5)
turtle.done()
