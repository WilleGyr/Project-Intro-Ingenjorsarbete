import pygame
import json
from pygame.locals import *

pygame.init()

screen_width = 1280
screen_height = 720

# Sets the screen resolution
screen = pygame.display.set_mode((screen_width, screen_height))

# Sets the name of the window to "Platformer"
pygame.display.set_caption('Platformer')

tile_size = 20

class World():
	def __init__(self, data):
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
				col_count += 1
			row_count += 1

	def draw(self):
		# Goes through every tile in the tile list
		for tile in self.tile_list:
			# Renders the tile at its specified position
			screen.blit(tile[0], tile[1])


# Imports the tilemaps for every level from json files
with open ("testmap.json", "r") as file4:
	testmap = json.load(file4)

with open ("level1.json", "r") as file1:
	level1 = json.load(file1)
	
with open ("level2.json", "r") as file2:
	level2 = json.load(file2)

with open ("level3.json", "r") as file3:
	level3 = json.load(file3)

# Imports the background image
bg = pygame.image.load("Data_files/images/himmel.png")

# Creates a world objects of every tilemap
world = World(testmap)
world_level1 = World(level1)
world_level2 = World(level2)
world_level3 = World(level3)

# Sets the chosen world to the test map for now
selectedWorld = world

run = True
while run:
	# Sets the bakground image
	screen.blit(bg, (0, 0))
	
	# Renders the selected world
	selectedWorld.draw()
	for event in pygame.event.get():

		# Exits the application if the window close button is pressed
		if event.type == pygame.QUIT:
			run = False
			
		# Changes the map between level 1, 2, 3 and 4  (test map)
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_1:
				selectedWorld = world_level1
			if event.key == pygame.K_2:
				selectedWorld = world_level2
			if event.key == pygame.K_3:
				selectedWorld = world_level3
			if event.key == pygame.K_4:
				selectedWorld = world
	pygame.display.update()

pygame.quit()
