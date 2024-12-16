import turtle

pen = turtle.Turtle()

pen.shape("turtle")
length = 100
num_petals = 9
for square in range(num_petals):
    for side in range(4):
        pen.forward(length)
        pen.right(90)
    pen.right(360 / num_petals)

pen.hideturtle()

screen = turtle.getscreen()
screen.setup(length * 4, length * 4)
screen.getcanvas().postscript(file="star.ps")
turtle.done()
