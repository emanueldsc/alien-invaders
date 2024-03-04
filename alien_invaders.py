import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
	
	# Start the game and add object to screen
	pygame.init()
	ia_settings = Settings()
	screen = pygame.display.set_mode((ia_settings.screen_width, ia_settings.screen_heigth))
	pygame.display.set_caption('Alien Invaders')
	ship = Ship(ia_settings, screen)
	
	# Start principal while
	while True:
		# Liste principal keyboard events and mice
		gf.check_events(ship)
		ship.update()
		gf.update_screen(ia_settings, screen, ship)

run_game()