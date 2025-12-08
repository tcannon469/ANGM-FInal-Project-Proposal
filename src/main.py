import pygame
import sys
import os
from levelmaps import LEVEL_MAPS

# ---------------------------------------------------
# GLOBAL SETTINGS
# ---------------------------------------------------
WIDTH, HEIGHT = 800, 600
TILE_SIZE = 32
FPS = 60

SKY_BLUE = (135, 206, 235)
GREEN = (0, 200, 0)
BROWN = (139, 69, 19)
RED = (200, 50, 50)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PLAYER_ASSET_DIR = os.path.join(BASE_DIR, "..", "assets", "player")

print("Looking for assets in:", PLAYER_ASSET_DIR)  # DEBUG

# ---------------------------------------------------
# PLAYER CLASS
# ---------------------------------------------------
class Player:
    def __init__(self, x, y):
        # Collision rectangle
        self.rect = pygame.Rect(x, y, TILE_SIZE, int(TILE_SIZE * 1.5))
        self.color = RED  # fallback

        # Physics
        self.vel_x = 0
        self.vel_y = 0
        self.speed = 4
        self.jump_power = 12
        self.gravity = 0.5
        self.max_fall_speed = 15
        self.on_ground = True

        # Animation state
        self.state = "idle"          # "idle", "run", "jump", "fall"
        self.facing_right = True
        self.frame_index = 0.0
        self.anim_speed = 0.12      # good for 2-frame run

        # Load animation frames
        self.animations = self.load_animations()
        self.image = self.animations["idle"][0] if self.animations["idle"] else None

    # ----------------- LOAD ANIMATIONS -----------------
    def load_animations(self):
        animations = {}

        def load_and_scale(filename):
            path = os.path.join(PLAYER_ASSET_DIR, filename)
            if not os.path.exists(path):
                return None
            img = pygame.image.load(path).convert_alpha()
            return pygame.transform.scale(img, (self.rect.width, self.rect.height))

        # idle.png (single frame)
        idle_frames = []
        idle_img = load_and_scale("idle.png")
        if idle_img:
            idle_frames.append(idle_img)
        animations["idle"] = idle_frames

        # run1.png, run2.png (can add run3 later if you want)
        run_frames = []
        for i in range(1, 4):  # will load run1, run2, run3 if present
            img = load_and_scale(f"run{i}.png")
            if img:
                run_frames.append(img)
        if not run_frames:
            run_frames = idle_frames.copy()
        animations["run"] = run_frames

        # jump.png
        jump_frames = []
        jump_img = load_and_scale("jump.png")
        if jump_img:
            jump_frames.append(jump_img)
        else:
            jump_frames = idle_frames.copy()
        animations["jump"] = jump_frames

        # fall.png
        fall_frames = []
        fall_img = load_and_scale("fall.png")
        if fall_img:
            fall_frames.append(fall_img)
        else:
            fall_frames = jump_frames.copy()
        animations["fall"] = fall_frames

        return animations

    # ----------------- INPUT -----------------
    def handle_input(self):
        keys = pygame.key.get_pressed()
        self.vel_x = 0

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.vel_x = -self.speed
            self.facing_right = False
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.vel_x = self.speed
            self.facing_right = True

        if (keys[pygame.K_SPACE] or keys[pygame.K_UP] or keys[pygame.K_w]) and self.on_ground:
            self.vel_y = -self.jump_power
            self.on_ground = False

    # ----------------- PHYSICS -----------------
    def apply_gravity(self):
        self.vel_y += self.gravity
        if self.vel_y > self.max_fall_speed:
            self.vel_y = self.max_fall_speed

    def move_and_collide(self, tiles):
        # horizontal
        self.rect.x += self.vel_x
        for tile in tiles:
            if self.rect.colliderect(tile):
                if self.vel_x > 0:
                    self.rect.right = tile.left
                elif self.vel_x < 0:
                    self.rect.left = tile.right

        # vertical
        self.rect.y += self.vel_y
        self.on_ground = False
        for tile in tiles:
            if self.rect.colliderect(tile):
                if self.vel_y > 0:  # falling
                    self.rect.bottom = tile.top
                    self.vel_y = 0
                    self.on_ground = True
                elif self.vel_y < 0:  # going up, hit underside
                    self.rect.top = tile.bottom
                    self.vel_y = 0

    # ----------------- STATE & ANIMATION -----------------
    def update_state(self):
        if not self.on_ground:
            if self.vel_y < 0:
                self.state = "jump"
            else:
                self.state = "fall"
        else:
            if self.vel_x != 0:
                self.state = "run"
            else:
                self.state = "idle"

    def animate(self):
        frames = self.animations.get(self.state, [])
        if not frames:
            self.image = None
            return

        self.frame_index += self.anim_speed
        if self.frame_index >= len(frames):
            self.frame_index = 0.0

        frame = frames[int(self.frame_index)]
        if not self.facing_right:
            frame = pygame.transform.flip(frame, True, False)
        self.image = frame

    # ----------------- UPDATE & DRAW -----------------
    def update(self, tiles):
        self.handle_input()
        self.apply_gravity()
        self.move_and_collide(tiles)
        self.update_state()
        self.animate()

    def reached_end(self, level_width_pixels):
        return self.rect.right >= level_width_pixels

    def draw(self, surface, camera_x):
        draw_rect = self.rect.copy()
        draw_rect.x -= camera_x
        if self.image:
            surface.blit(self.image, draw_rect.topleft)
        else:
            pygame.draw.rect(surface, self.color, draw_rect)


# ---------------------------------------------------
# LEVEL BUILDING
# ---------------------------------------------------
def build_level(level_map):
    tiles = []
    player_start_pos = (0, 0)

    for row_index, row in enumerate(level_map):
        for col_index, tile in enumerate(row):
            x = col_index * TILE_SIZE
            y = row_index * TILE_SIZE
            if tile == "X":
                tiles.append(pygame.Rect(x, y, TILE_SIZE, TILE_SIZE))
            elif tile == "P":
                player_start_pos = (x, y)

    return tiles, player_start_pos


# ---------------------------------------------------
# CAMERA
# ---------------------------------------------------
def get_camera_x(player, level_width_pixels):
    target_x = player.rect.centerx - WIDTH // 2
    return max(0, min(target_x, level_width_pixels - WIDTH))


# ---------------------------------------------------
# MAIN GAME LOOP
# ---------------------------------------------------
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Platformer with Adventurer")
    clock = pygame.time.Clock()

    current_level = 0
    tiles, player_pos = build_level(LEVEL_MAPS[current_level])
    player = Player(*player_pos)

    # width based on number of columns in the row
    level_width_pixels = len(LEVEL_MAPS[current_level][0]) * TILE_SIZE
    running = True

    while running:
        dt = clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        player.update(tiles)

        # next level when player reaches end
        if player.reached_end(level_width_pixels):
            current_level += 1
            if current_level >= len(LEVEL_MAPS):
                running = False
            else:
                tiles, player_pos = build_level(LEVEL_MAPS[current_level])
                player = Player(*player_pos)
                level_width_pixels = len(LEVEL_MAPS[current_level][0]) * TILE_SIZE

        camera_x = get_camera_x(player, level_width_pixels)

        # draw
        screen.fill(SKY_BLUE)

        for tile in tiles:
            r = tile.copy()
            r.x -= camera_x
            pygame.draw.rect(screen, BROWN, r)
            grass = pygame.Rect(r.x, r.y, r.width, 6)
            pygame.draw.rect(screen, GREEN, grass)

        player.draw(screen, camera_x)
        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
