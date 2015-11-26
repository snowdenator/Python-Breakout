import sys, pygame, random, time, numpy

pygame.init()

ScreenSize = width, height = 1000, 1000 #Should be in multiples of 10!
Screen = pygame.display.set_mode(ScreenSize)
pygame.display.set_caption("Breakout")

PongBallSpeed = [1, 2]
PongBallRect = pygame.Rect((width / 2, height / 2), (10, 10))

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

	PongBallRect = PongBallRect.move(PongBallSpeed)

	if PongBallRect.left < 0 or PongBallRect.right > width:
		PongBallSpeed[0] = -PongBallSpeed[0]
	
	if PongBallRect.top < 0 or PongBallRect.bottom > height:
		PongBallSpeed[1] = -PongBallSpeed[1]

	#Screen.fill((0, 0, 0))
	pygame.draw.circle(Screen, (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)), PongBallRect.center, 10)
	pygame.display.update()