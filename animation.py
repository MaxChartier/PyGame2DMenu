import sys
import pygame


class Archer(pygame.sprite.Sprite):

    def __init__(self, pos_x, pos_y):

        super().__init__()

        self.sprites_archer = []

        # Define the size of the sprites (in pixels)
        gif_size = (66, 90)

        sprite_archer_0 = pygame.image.load("Images/archerAnimation/frame_01_delay-0.13s.gif").convert_alpha()
        sprite_archer_0 = pygame.transform.scale(sprite_archer_0, gif_size)
        sprite_archer_1 = pygame.image.load("Images/archerAnimation/frame_02_delay-0.13s.gif").convert_alpha()
        sprite_archer_1 = pygame.transform.scale(sprite_archer_1, gif_size)
        sprite_archer_2 = pygame.image.load("Images/archerAnimation/frame_03_delay-0.13s.gif").convert_alpha()
        sprite_archer_2 = pygame.transform.scale(sprite_archer_2, gif_size)
        sprite_archer_3 = pygame.image.load("Images/archerAnimation/frame_04_delay-0.13s.gif").convert_alpha()
        sprite_archer_3 = pygame.transform.scale(sprite_archer_3, gif_size)
        sprite_archer_4 = pygame.image.load("Images/archerAnimation/frame_05_delay-0.13s.gif").convert_alpha()
        sprite_archer_4 = pygame.transform.scale(sprite_archer_4, gif_size)
        sprite_archer_5 = pygame.image.load("Images/archerAnimation/frame_06_delay-0.13s.gif").convert_alpha()
        sprite_archer_5 = pygame.transform.scale(sprite_archer_5, gif_size)
        sprite_archer_6 = pygame.image.load("Images/archerAnimation/frame_07_delay-0.13s.gif").convert_alpha()
        sprite_archer_6 = pygame.transform.scale(sprite_archer_6, gif_size)
        sprite_archer_7 = pygame.image.load("Images/archerAnimation/frame_08_delay-0.13s.gif").convert_alpha()
        sprite_archer_7 = pygame.transform.scale(sprite_archer_7, gif_size)
        sprite_archer_8 = pygame.image.load("Images/archerAnimation/frame_09_delay-0.13s.gif").convert_alpha()
        sprite_archer_8 = pygame.transform.scale(sprite_archer_8, gif_size)
        sprite_archer_9 = pygame.image.load("Images/archerAnimation/frame_10_delay-0.13s.gif").convert_alpha()
        sprite_archer_9 = pygame.transform.scale(sprite_archer_9, gif_size)
        sprite_archer_10 = pygame.image.load("Images/archerAnimation/frame_11_delay-0.13s.gif").convert_alpha()
        sprite_archer_10= pygame.transform.scale(sprite_archer_10, gif_size)
        sprite_archer_11= pygame.image.load("Images/archerAnimation/frame_12_delay-0.13s.gif").convert_alpha()
        sprite_archer_11= pygame.transform.scale(sprite_archer_11, gif_size)
        sprite_archer_12 = pygame.image.load("Images/archerAnimation/frame_13_delay-0.13s.gif").convert_alpha()
        sprite_archer_12 = pygame.transform.scale(sprite_archer_12, gif_size)
        sprite_archer_13 = pygame.image.load("Images/archerAnimation/frame_14_delay-0.13s.gif").convert_alpha()
        sprite_archer_13 = pygame.transform.scale(sprite_archer_13, gif_size)
        sprite_archer_14 = pygame.image.load("Images/archerAnimation/frame_15_delay-0.13s.gif").convert_alpha()
        sprite_archer_14 = pygame.transform.scale(sprite_archer_13, gif_size)

        # Put the sprites in the sprites array
        self.sprites_archer.append(sprite_archer_0)
        self.sprites_archer.append(sprite_archer_1)
        self.sprites_archer.append(sprite_archer_2)
        self.sprites_archer.append(sprite_archer_3)
        self.sprites_archer.append(sprite_archer_4)
        self.sprites_archer.append(sprite_archer_5)
        self.sprites_archer.append(sprite_archer_6)
        self.sprites_archer.append(sprite_archer_7)
        self.sprites_archer.append(sprite_archer_8)
        self.sprites_archer.append(sprite_archer_9)
        self.sprites_archer.append(sprite_archer_10)
        self.sprites_archer.append(sprite_archer_11)
        self.sprites_archer.append(sprite_archer_12)
        self.sprites_archer.append(sprite_archer_13)
        self.sprites_archer.append(sprite_archer_14)


        # The first image to display corresponds to the image at index 0.
        # Then the index will be increased by one until reaching the maximum index.
        self.actual_sprite = 0
        self.image = self.sprites_archer[self.actual_sprite]

        # Creating a rectangle around the image in order to place it wherever we want
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def update(self, speed):
        # We go to the next image in the array (we use a value inferior to 0 to slow down the animation because of the
        # int casting will round it to the next integer)
        self.actual_sprite += speed

        # the indexes of the array are limited, there will be an error if it goes past the maximum index
        if self.actual_sprite >= len(self.sprites_archer):
            self.actual_sprite = 0

        # We also need to update the image to be displayed
        self.image = self.sprites_archer[int(self.actual_sprite)]

# General setup
pygame.init()
clock = pygame.time.Clock()
# Screen/Window parameter
#screen_width = 1200
#screen_height = 600
#screen = pygame.display.set_mode((screen_width, screen_height))
#pygame.display.set_caption("archer GIF animation")

# Creating sprites and form a group with them for the archer
moving_sprites_archer = pygame.sprite.Group()
archer = Archer(300, 400)
moving_sprites_archer.add(archer)

key_pressed_is = pygame.key.get_pressed()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Shut down the pygame library
            pygame.quit()
            # Exit the program
            sys.exit()
    moving_sprites_archer.draw(screen)
    moving_sprites_archer.update(0.2)
    pygame.display.flip()
    clock.tick(60)

    # We need to draw the elements:
    # - Screen color
    screen.fill((214, 159, 126))

    # - Draw the sprites


