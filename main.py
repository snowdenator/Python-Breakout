'''
PyGame breakout
Callum Snowden
'''

import sys, pygame, random, time

pygame.init()

ScreenSize = width, height = 600, 400
BoxSpeed = [1, 1]
Black = 0,0,0

Screen = pygame.display.set_mode(ScreenSize)

CurrentJoystick = pygame.joystick.Joystick(0)
CurrentJoystick.init()

def maprange( a, b, s):
	(a1, a2), (b1, b2) = a, b
	return  b1 + ((s - a1) * (b2 - b1) / (a2 - a1))

for x in xrange(0, width, 10):
	for y in xrange(0, height / 2, 10):
		pygame.draw.rect(Screen, (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)), (x, y, 9, 9), 0)
	pass
pass

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

	JoystickXVal = int(maprange((-1, 1), (0, 600), CurrentJoystick.get_axis(0))) #Xbox360 left joy X axis
	JoystickYVal = int(maprange((-1, 1), (0, 400), CurrentJoystick.get_axis(1))) #Xbox360 left joy Y axis

	#Screen.fill(Black)
	pygame.draw.circle(Screen, (random.randint(127, 255), random.randint(127, 255), random.randint(127, 255)), (JoystickXVal, JoystickYVal), 5, 0)
	#Screen.set_at((JoystickXVal, JoystickYVal), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
	pygame.display.update()