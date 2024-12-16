import turtlethread


needle = turtlethread.Turtle()

# Create the first row: running stitch
with needle.running_stitch(20):
    needle.forward(500)

# Move down one row to the next start position
with needle.jump_stitch(30):
    needle.backward(500)
    needle.right(90)
    needle.forward(250)
    needle.right(-90)

# Create the second row: triple stitch
with needle.triple_stitch(30):
    needle.forward(500)

# Move down one row to the next start position
with needle.jump_stitch(30):
    needle.backward(500)
    needle.right(90)
    needle.forward(250)
    needle.right(-90)

# Create the second row: jump stitch
with needle.running_stitch(20):
    needle.forward(150)
with needle.jump_stitch():
    needle.forward(200)
with needle.running_stitch(30):
    needle.forward(150)

# Save the pattern
needle.save("stitch_types.jef")
needle.show_info()
needle.visualise(scale=0.5)
