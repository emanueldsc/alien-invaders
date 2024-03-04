import sys
import pygame

def run_game():
	# Start the game and add object to screen
	pygame.init()
	screen = pygame.display.set_mode((1200,800))
	pygame.display.set_caption('Alien Invaders')
	# Start princiap while
	while True:
		# Liste principal keyboard events and mice
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			# Show last screen see
			pygame.display.flip()

run_game()