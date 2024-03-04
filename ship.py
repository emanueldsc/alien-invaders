import pygame

class Ship():

	def __init__(self, ai_settings, screen):
		# Initial position startship
		self.screen = screen
		self.ai_settings = ai_settings
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		self.center = float(self.rect.centerx)
		self.moving_rigth = False
		self.moving_left = False

	def update(self):
		# Update ship position accoding moviment flag
		if self.moving_rigth:
			self.rect.centerx += self.ai_settings.ship_speed_factor
		if self.moving_left:
			self.rect.centerx -= self.ai_settings.ship_speed_factor

	def blitme(self):
		# Draw startship in curent position
		self.screen.blit(self.image, self.rect)