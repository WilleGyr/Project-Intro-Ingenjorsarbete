import pygame
import json
from pygame.locals import *

class World():
	def __init__(self, data):
		tile_size = 20
		self.tile_list = []

		# Imports selected images
		dirt_img = pygame.image.load('Data_files/images/tiles/grass/5.png')
		grass_img = pygame.image.load('Data_files/images/tiles/grass/1.png')
		grass_r_img = pygame.image.load('Data_files/images/tiles/grass/2.png')
		grass_l_img = pygame.image.load('Data_files/images/tiles/grass/0.png')
		dirt_l_img = pygame.image.load('Data_files/images/tiles/grass/7.png')
		dirt_r_img = pygame.image.load('Data_files/images/tiles/grass/3.png')
		stone_l_img = pygame.image.load('Data_files/images/tiles/stone/0.png')
		stone_r_img = pygame.image.load('Data_files/images/tiles/stone/2.png')
		stone_t_img = pygame.image.load('Data_files/images/tiles/stone/1.png')
		stone_img = pygame.image.load('Data_files/images/tiles/stone/5.png')
		border_img = pygame.image.load('Data_files/images/border.png')
		cloud1_img = pygame.image.load('Data_files/images/clouds/cloud_1.png')
		tree_img = pygame.image.load('Data_files/images/tiles/large_decor/2.png')
		bush_img = pygame.image.load('Data_files/images/tiles/large_decor/1.png')
		crate_img = pygame.image.load('Data_files/images/tiles/decor/3.png')
		flower1_img = pygame.image.load('Data_files/images/tiles/decor/2.png')
		rock_img = pygame.image.load('Data_files/images/tiles/large_decor/0.png')
		level1_img = pygame.image.load('Data_files/images/border_level1.png')
		level2_img = pygame.image.load('Data_files/images/border_level2.png')
		level3_img = pygame.image.load('Data_files/images/border_level3.png')
		

		row_count = 0
		
		# Goes through every row
		for row in data:
			col_count = 0
			# Goes through every column
			for tile in row:
				if tile == 1:
					# Scale the image to the right size
					img = pygame.transform.scale(border_img, (tile_size, tile_size))
					
					# Creates a rectangle to represent the image's position and dimensions
					img_rect = img.get_rect()
					
					# The x position of the tile
					img_rect.x = col_count * tile_size
					
					# The y position of the tile
					img_rect.y = row_count * tile_size
					
					# Creates a tile with the image and its position
					tile = (img, img_rect)
					
					# Adds the tile to the tile list
					self.tile_list.append(tile)
					
					# Repeats for every image
				if tile == 2:
					img = pygame.transform.scale(grass_img, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 3:
					img = pygame.transform.scale(grass_r_img, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 4:
					img = pygame.transform.scale(grass_l_img, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 5:
					img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 6:
					img = pygame.transform.scale(stone_l_img, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 7:
					img = pygame.transform.scale(stone_r_img, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 8:
					img = pygame.transform.scale(stone_t_img, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 9:
					img = pygame.transform.scale(stone_img, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 10:
					img = pygame.transform.scale(cloud1_img, (tile_size+150, tile_size+30))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 11:
					img = pygame.transform.scale(tree_img, (tile_size+66, tile_size+100))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 12:
					img = pygame.transform.scale(bush_img, (tile_size+30, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 13:
					img = pygame.transform.scale(crate_img, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 14:
					img = pygame.transform.scale(rock_img, (tile_size+50, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 15:
					img = pygame.transform.scale(flower1_img, (tile_size+15, tile_size+20))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 16:
					img = pygame.transform.scale(dirt_l_img, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 17:
					img = pygame.transform.scale(dirt_r_img, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 18:
					img = pygame.transform.scale(level1_img, (tile_size+100, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 19:
					img = pygame.transform.scale(level2_img, (tile_size+100, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 20:
					img = pygame.transform.scale(level3_img, (tile_size+100, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				col_count += 1
			row_count += 1

	def draw(self, game):
		# Goes through every tile in the tile list
		for tile in self.tile_list:
			# Renders the tile at its specified position
			game.screen.blit(tile[0], tile[1])
