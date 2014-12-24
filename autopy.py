import autopy
import math
import time
import random 

def hello_world():
	autopy.alert.alert("Hello, world")
hello_world()

autopy.mouse.move(1,1)

autopy.mouse.smooth_move(1, 1)

TWO_Pi = math.pi * 2.0
def sine_mouse_wave():
	"""moves mouse in a sine wave from the left 
	edge to the right of the screen. """

	width, height = autoy.screen.get_size()
	height /=2
	height -= 10 #stay within screen 

	for x in xrange(width):
		y = int(height*math.sin((TWO_Pi * x) / width) + height)
		autopy.mouse.move(x, y)
		time.sleep(random.uniform(0.001, 0.003))

sine_mouse_wave()
