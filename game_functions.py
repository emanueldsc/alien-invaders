import sys
import pygame

def check_events(ship):
	# Responds to events when keyborad press
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				ship.rect.centerx += 1

def update_screen(ia_settings, screen, ship):
	# Update images in screen to new screen
	screen.fill(ia_settings.bg_color)
	ship.blitme()
	pygame.display.flip()