import turtle

pen = turtle.Turtle()

for _ in range(11):
  pen.forward(100)
  pen.right(5*360/11)

turtle.done()
