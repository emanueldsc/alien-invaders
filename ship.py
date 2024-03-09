import pygame

class Ship():

	def __init__(self, ai_settings, screen): # u
		# Initial position startship
		self.screen = screen
		self.ai_settings = ai_settings # v
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		self.center = float(self.rect.centerx) # w
		self.moving_rigth = False
		self.moving_left = False

	def update(self):
		# Update ship position accoding moviment flag
		if self.moving_rigth and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > self.screen_rect.left:
			self.center -= self.ai_settings.ship_speed_factor
		self.rect.centerx = self.center

	def blitme(self):
		# Draw startship in curent position
		self.screen.blit(self.image, self.rect)