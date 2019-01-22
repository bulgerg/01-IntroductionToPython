"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and George Bulger.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
#window.tracer(100)

turtle_a=rg.SimpleTurtle('turtle')
turtle_a.pen=rg.Pen('teal',1)
turtle_a.speed=900
turtle_a.pen_up()
turtle_a.backward(135)
turtle_a.left(20)

turtle_a.pen_down()

for k in range(50):
    turtle_a.forward(100)
    turtle_a.right(119)



turtle_b=rg.SimpleTurtle('triangle')
turtle_b.pen=rg.Pen('navy',1)
turtle_b.speed=900
turtle_b.pen_up()
turtle_b.backward(200)
turtle_b.left(90)
turtle_b.backward(260)
turtle_b.pen_down()


for k in range(135):
    turtle_b.forward(500)
    turtle_b.right(129)

window.close_on_mouse_click()
