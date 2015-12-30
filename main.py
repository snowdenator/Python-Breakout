'''
PyGame breakout
Callum Snowden

CONTROLS:
Left stick: X(/Y) of paddle
Start button: pause
Back button: exit

To start game:
Use (LB)/(RB) to select ball speed (default 3)
(A) to confirm
Then (Start) to (un)pause the game
(Back) to exit
'''

import sys, pygame, random, time, numpy

pygame.init()

ScreenSize = width, height = 800, 600 #Should be in multiples of 10!

CurrentPixels = numpy.ones((width / 10, (height / 2) / 10), dtype=int) #Generate array for storing whether a "pixel" is there or not

Screen = pygame.display.set_mode(ScreenSize, pygame.HWSURFACE | pygame.DOUBLEBUF)
pygame.display.set_caption("Breakout")

CurrentJoystick = pygame.joystick.Joystick(0)
CurrentJoystick.init()

PaddleWidth = 300 #Paddle width

PongBallRect = pygame.Rect((width / 2, int(height * 0.6)), (10, 10)) #Calculate initial rectangle for ball

clock = pygame.time.Clock() #Used to get FPS

GREY = pygame.Color(128, 128, 128)

def maprange( a, b, s): #Useful map function
	(a1, a2), (b1, b2) = a, b
	return  b1 + ((s - a1) * (b2 - b1) / (a2 - a1))

def round_down(num, divisor):
    return num - (num%divisor)

#Generate playfield
#Divided by 10 because each "pixel" is 10x10px
for y in xrange(0, (height / 2) / 10): #Divide by 2 - we only want half the window filled
	for x in xrange(0, width / 10):
		if CurrentPixels[x][y] == 1:
			pygame.draw.rect(Screen, (128, 128, 128), (x*10, y*10, 10, 10), 0)

def setup(): #Setup routine
	print("Enter game setup")

	CurrentPixels = numpy.ones((width / 10, (height / 2) / 10), dtype=int) #Restart with a fresh array (ie full screen)

	#Generate playfield
	#Divided by 10 because each "pixel" is 10x10px
	for y in xrange(0, (height / 2) / 10): #Divide by 2 - we only want half the window filled
		for x in xrange(0, width / 10):
			pygame.draw.rect(Screen, (128, 128, 128), (x*10, y*10, 10, 10), 0)

	pygame.draw.circle(Screen, (255, 255, 255), PongBallRect.center, 10) #Redraw ball

	pygame.display.update()

	print("Exit game setup")

	mainLoop() #Enter main loop

def mainLoop():

	GamePaused = True

	PongBallRect = pygame.Rect((width / 2, int(height * 0.6)), (10, 10)) #Make rectangle again

	CurrentPixels = numpy.ones((width / 10, (height / 2) / 10), dtype=int) #Restart with a fresh array (ie full screen)

	PongBallSpeed = [3, 3] #Ball movement speed

	Score = 0

	#Generate playfield
	#Divided by 10 because each "pixel" is 10x10px
	for y in xrange(0, (height / 2) / 10): #Divide by 2 - we only want half the window filled
		for x in xrange(0, width / 10):
			pygame.draw.rect(Screen, (128, 128, 128), (x*10, y*10, 10, 10), 0)

	BallSpeedLoop = True

	print("Entered difficulty selection loop")

	while BallSpeedLoop:
		for event in pygame.event.get():
			if event.type == pygame.JOYBUTTONDOWN:
				if CurrentJoystick.get_button(4) == True and PongBallSpeed[0] > 0 and PongBallSpeed[1] > 0 and GamePaused == True:
					PongBallSpeed[0] -= 1
					PongBallSpeed[1] -= 1
					print("Ball speed X: {}".format(PongBallSpeed[0]))
					print("Ball speed Y: {}".format(PongBallSpeed[1]))
				if CurrentJoystick.get_button(5) == True and PongBallSpeed[0] < 7 and PongBallSpeed[1] < 7 and GamePaused == True:
					PongBallSpeed[0] += 1
					PongBallSpeed[1] += 1
					print("Ball speed X: {}".format(PongBallSpeed[0]))
					print("Ball speed Y: {}".format(PongBallSpeed[1]))

				if CurrentJoystick.get_button(0) == True:
					print("Entered game loop, game paused")
					BallSpeedLoop = False

				if CurrentJoystick.get_button(6) == True:
					sys.exit()
					
	while True:

		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()

			if event.type == pygame.JOYBUTTONDOWN:
				if CurrentJoystick.get_button(7) == True:
					GamePaused = not GamePaused
					print("Game paused: {}".format(GamePaused))

				if CurrentJoystick.get_button(6) == True:
					sys.exit()

		if GamePaused == False: #Game paused function

			JoystickXVal = int(maprange((-1, 1), (0, width), CurrentJoystick.get_axis(0))) #Xbox360 left joy X axis
			JoystickYVal = int(maprange((-1, 1), (height / 2, height), CurrentJoystick.get_axis(1))) #Xbox360 left joy Y axis, scaled to be in centre of lower screen

			Screen.fill((0, 0, 0)) #Erase screen to black

			#Redraw the pixel field (omitting black pixels)
			#Divided by 10 because each "pixel" is 10x10px
			for y in xrange(0, (height / 2) / 10): #Divide by 2 - we only want half the window filled
				for x in xrange(0, width / 10):
					if CurrentPixels[x][y] == 1:
						pygame.draw.rect(Screen, (128, 128, 128), (x*10, y*10, 10, 10), 0) #Draw grey pixel (ie pixel present)
					else:
						pygame.draw.rect(Screen, (0, 0, 0), (x*10, y*10, 10, 10), 0) #Draw black pixel (ie no pixel, it's been hit already)

			#Paddle = pygame.draw.rect(Screen, (255, 255, 255), (JoystickXVal, JoystickYVal, PaddleWidth, 10), 0)#(height * 0.75), 100, 10), 0)
			Paddle = pygame.draw.rect(Screen, (255, 255, 255), (JoystickXVal, int(height * 0.75), PaddleWidth, 10), 0)

			#pygame.display.update()

			PongBallRect = PongBallRect.move(PongBallSpeed) #Move the specified amount of pixels, hence effective speed

			if PongBallRect.left <= 0 or PongBallRect.right >= width: #Bounce off the sides
				PongBallSpeed[0] = -PongBallSpeed[0]
	
			if PongBallRect.top <= 0: #Bounce off the top
				PongBallSpeed[1] = -PongBallSpeed[1]


			if PongBallRect.bottomleft > Paddle.topleft and PongBallRect.bottomright < Paddle.topright and PongBallRect.bottom > Paddle.top and PongBallRect.bottom < Paddle.bottom: #Add margin for touching paddle top (useful for quasi-3D)
				PongBallSpeed[1] = -PongBallSpeed[1]

			if PongBallRect.bottom > height: #If ball has left screen on bottom, start again
				print("Score: {}".format(Score))
				setup()

			#print("Pixel at ball X: {}".format((round_down(PongBallRect.centerx, 10) / 10))) #Debug the ball location
			#print("Pixel at ball Y: {}".format((round_down(PongBallRect.centery, 10) / 10)))

			#--BALL PIXEL CHECKING--
			if Screen.get_at((PongBallRect.centerx, PongBallRect.centery)) == GREY: #If the ball is sat over a grey pixel
				CurrentPixels[round_down(PongBallRect.centerx, 10) / 10][round_down(PongBallRect.centery, 10) / 10] = 0 #Remove it
				if (round_down(PongBallRect.centerx, 10) / 10) + 1 < 80:
					CurrentPixels[(round_down(PongBallRect.centerx, 10) / 10) + 1][round_down(PongBallRect.centery, 10) / 10] = 0 #Remove it
				PongBallSpeed[0] = PongBallSpeed[0] #Flip the directions
				PongBallSpeed[1] = -PongBallSpeed[1]
				Score += 1

			#--FINAL DRAWING--
			pygame.draw.circle(Screen, (255, 255, 255), PongBallRect.center, 10) #Draw the ball in it's new position

			pygame.display.flip() #Render everything to screen
			clock.tick()

if __name__ == '__main__': #Run when program starts
	setup()