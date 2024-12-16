import turtlethread

pen = turtlethread.Turtle()

length = 200
num_petals = 9
with pen.triple_stitch(30):  # three mm between each stitch
    for square in range(num_petals):
        for side in range(4):
            pen.forward(length)
            pen.right(90)
        pen.right(360 / num_petals)

pen.show_info()
pen.save("star.jef")  # JEF-files are the best for this machine
pen.visualise()
