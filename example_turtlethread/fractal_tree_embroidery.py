# Inspired by https://medium.com/@limkao/teach-you-to-draw-a-christmas-tree-in-python-80f4bcf8c9d5

from turtlethread import Turtle


def draw_branch(d, s, turtle):
    """Each branch consists of two "side-branches" and a "main branch".

    Once a branch is drawn, the turtle is at the same place as it started
    """
    if d <= 0:
        return

    # Move a little bit forwards before drawing the side branches
    turtle.forward(s)

    # Draw the right branch. The turtle is where it started after these two lines
    turtle.right(120)
    draw_branch(d - 3, s * 0.5, turtle)

    # Draw the left branch. The turtle is where it started after these two lines
    turtle.right(120)
    draw_branch(d - 3, s * 0.5, turtle)

    # Rotate back to the initial heading
    turtle.right(120)

    # Draw the main branch. The turtle is where it started after this line
    draw_branch(d - 1, s * 0.8, turtle)

    # Move back to where the turtle started
    turtle.backward(s)


n = 200

turtle = Turtle()

# The christmas tree is drawn as one large branch
with turtle.running_stitch(20):
    draw_branch(11, n, turtle)

turtle.save("christmas_tree.jef")
turtle.show_info()
