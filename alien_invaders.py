import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
	# Start the game and add object to screen
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_heigth))
	pygame.display.set_caption('Alien Invaders')
	ship = Ship(ai_settings, screen)
	bullets = Group()
	
	# Start principal while
	while True:
		# List principal keyboard events and mice
		gf.check_events(ai_settings, screen, ship, bullets)
		ship.update()
		gf.update_bullets(bullets)
		gf.update_screen(ai_settings, screen, ship, bullets)

run_game()