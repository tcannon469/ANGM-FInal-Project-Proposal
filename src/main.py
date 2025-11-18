import random
import pygame
import sys
# Global constants and settings
import level_maps

WIDTH, HEIGHT = 800, 600
TILESIZE = 32
FPS = 60

clock = pygame.time.Clock()

def build_level(level_map):
    # Function to build the level based on the level_map found in file level_maps.py
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