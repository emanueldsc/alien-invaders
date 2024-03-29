import sys
import pygame

def check_events(ship):
	# Responds to events when keyborad press
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()		
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ship)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)

def update_screen(ia_settings, screen, ship):
	# Update images in screen to new screen
	screen.fill(ia_settings.bg_color)
	ship.blitme()
	pygame.display.flip()

def check_keydown_events(event, ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_rigth = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True

def check_keyup_events(event, ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_rigth = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False