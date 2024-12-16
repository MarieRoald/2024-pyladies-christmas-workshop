# Tips and tricks for using the embroidery machine

## Designing patterns

The embroidery machine is a sewing machine that moves the fabric for us, which puts several limitations on how we should design patterns:

* Don't have many stitches very close to each other. This leads to buildup and can break the needle  
* Don't change colours too often. This requires rethreading the machine which is a bit annoying to do many times (also, TurtleThread doesn't support color changes yet)  
* Don't have too many "jumps", this requires fastening the thread for each jump, which can be slow.

However, don't let these limitations discourage you. Afterall, constraints breeds creativity!

Here are some things you can do (and are encouraged to also):

* Use "triple stitches", where the needle moves forwards, backwards and forwards again. This leads to a nicely defined line  
* Look up some inspiration from single line drawings and see if you can do something similar in Python  
* Remember that symmetry and loops can lead to some very nice patterns!

## Embroidering

To embroider, simply copy your design to a USB-pen and plug it into the embroidery machine. 

There are three things that make or break your embroidery: tension, tension and tension. When we set up the machine for use, we need to do our best to make sure that the tension is good. We'll get a tangled thread if the tension is wrong. There are somethings we can do to make sure the tension is good:

* Be extra careful when threading the machine  
* Use a special bobbin-thread named "bobbinette". It's black, but we won't see it on the right side if the tension is correct  
* Use polysheen, silk or rayon threads as the main thread.  
* Use stabilizer (vlieseline). I'm a fan of tearaway, but washaway works well too. Iron-on is not necessary. Newspapers work really well for dark fabrics (two pages behind the fabric)  
* Embroider on woven or felted fabrics (i.e. not knit or stretch)

## Debugging the machine

The first thing to do if the machine behaves weirdly is to rethread the bobbin-thread (maybe the main thread too) and turn down the speed. If that doesn't work: throw away the bobbin-thread and spool up some new. The machine is extremely sensitive to the bobbin.

If that doesn't work, change the needle. Needles get dull, and a dull needle can mess up with the timing of the machine.  Finally, try a different pattern and see if you still have trouble. If not, then your design might be difficult to embroider.

# Tips and tricks for using the craft cutter

## Using the craft cutter with Turtle drawings

Unfortunately, there is no direct interface that will let us control the craft cutter with Python. However, "[Cricut design space](https://design.cricut.com/)", the program we use for communicating with the machine, lets us cut (and draw) based on SVG-files. So to use the craft cutter, we can save our Turtle drawings as postscript files (`turtle.getscreen().getcanvas().postscript(file="drawing.ps")`) that we can convert to SVG files using either an [online converter](https://cloudconvert.com/eps-to-svg) or tools like [InkScape](https://inkscape.org/).

So in summary, to use the craft-cutter, you need to:

* Download and install "[Cricut design space](https://design.cricut.com/)" (or send it to us by e-mail so we can use our computer)  
* Save the turtle drawing as a postscript file (`turtle.getscreen().getcanvas().postscript(file="drawing.ps")`)  
* Convert the postscript file to an SVG, e.g. using [online converter](https://cloudconvert.com/eps-to-svg) or tools like [InkScape](https://inkscape.org/)  
* Create a new project in Cricut design space and import the SVG.

## Tips and tricks when designing patterns

When you design patterns, you get a drawing that the craft cutter either follows with a knife or a foam pen (like a pen-plotter). This gives us much freedom when designing patterns.

Also, while the craft cutter can cut inside pieces that have been cut already, you shouldn't overdo it as the paper can move slightly. However, other than that, it's pretty forgiving.
