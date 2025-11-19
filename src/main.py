import random
import pygame
import sys
# Global constants and settings
from levelmaps import LEVEL_MAPS  

WIDTH, HEIGHT = 800, 600
TILESIZE = 32
FPS = 60

clock = pygame.time.Clock()

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 
# Function to build the level based on the level_map found in file level_maps.py
# Input: Level Map (2D List)
# Output: List of Tile Rects and Player Start Position  
# # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *    
def build_level(level_map):
    tiles = []
    for row_index, row in enumerate(level_map):
        for col_index, tile in enumerate(row):
            x = col_index * TILESIZE
            y = row_index * TILESIZE
            if tile == 'X':
                tiles.append(pygame.Rect(x, y, TILESIZE, TILESIZE))
            elif tile == 'P':
                player_start_pos = (x, y)
    return tiles, player_start_pos

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
# Player Class
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
Class Player:
    def __init__(self, position):
        self.rect = pygame.Rect(position[0], position[1], TILESIZE, TILESIZE)
        self.color = (0, 255, 0)  # Green color for the player

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)







# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
#                                Main Routine
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Final Projet - Thomas Cannon")

    tiles,playerPos = build_level(LEVEL_MAPS[0])
                                      # Generate a random color
    random_color = (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )

    # Fill the screen with the random color
    screen.fill(random_color)
    pygame.display.flip()

    # Main loop to keep the window open
    running = True
    dt = clock.tick(FPS)  # Amount of seconds between each loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        for tile in tiles:
            pygame.draw.rect(screen, (255, 255, 255), tile)
        pygame.display.flip()

    pygame.quit()
    sys.exit()    

if __name__ == "__main__":
    main()