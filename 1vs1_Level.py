# Importing pygame module
import time

import pygame
from pygame.locals import *
import button
from pygame import mixer
import math

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
        sprite_archer_10 = pygame.transform.scale(sprite_archer_10, gif_size)
        sprite_archer_11 = pygame.image.load("Images/archerAnimation/frame_12_delay-0.13s.gif").convert_alpha()
        sprite_archer_11 = pygame.transform.scale(sprite_archer_11, gif_size)
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


# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

# create the display surface object
# of specific dimension.
window = pygame.display.set_mode((600, 600))

# music import
mixer.init()
mixer.music.load('MusicMenu.mp3')
volume = 0.2
mixer.music.set_volume(volume)
pygame.init()
mixer.music.play()
music = True
Time=0
Time2=0
KeyTime = False
# create game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

# game variables
Game_over = False
game_paused = False
menu_state = "main"
lifes1 = 3
lifes2 = 3

# define fonts
font = pygame.font.SysFont("arial black", 40)

# define colours
TEXT_COL = (255, 255, 255)

# load button images
resume_img = pygame.image.load("Images/button_resume.png")
options_img = pygame.image.load("Images/button_options.png")
quit_img = pygame.image.load("Images/button_quit.png")
video_img = pygame.image.load('Images/button_video.png')
audio_img = pygame.image.load('Images/button_audio.png')
keys_img = pygame.image.load('Images/button_keys.png')
back_img = pygame.image.load('Images/button_back.png')

# create button instances
resume_button = button.Button(304, 125, resume_img, 1)
options_button = button.Button(297, 250, options_img, 1)
quit_button = button.Button(336, 375, quit_img, 1)
video_button = button.Button(226, 75, video_img, 1)
audio_button = button.Button(225, 150, audio_img, 1)
keys_button = button.Button(246, 295, keys_img, 1)
back_button = button.Button(332, 430, back_img, 1)


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


# creating actions
direction = True
directionArrow = True
directionArrow2 = True
direction2 = True
jump = False
jump1 = False
Fire = False
Fire1 = False
v_new = 5
m_new = 1


# Add caption in the window
pygame.display.set_caption('Player Movement')

# Initializing the clock
# Clocks are used to track and
# control the frame-rate of a game
clock = pygame.time.Clock()

# Add player sprite
image = pygame.image.load(r'Images/Player_image1.gif')
image = pygame.transform.scale(image, (66, 90))
image2 = pygame.image.load(r'Images/Player_image.png')
image2 = pygame.transform.scale(image2, (66, 90))
shoot1 = pygame.image.load(r'Images/ball1.png')
shoot = pygame.image.load(r'Images/ball2.png')

# Store the initial
# coordinates of the player in
# two variables i.e. x and y.
x1 = 600
y1 = 420
x = 150
y = 420
xb = -800
yb = -800
xb1 = -800
yb1 = -800
# Create a variable to store the
# velocity of player's movement
velocity = 1
vel = 9
mass = 1
vel1 = 10
mass1 = 1

moving_sprites_archer = pygame.sprite.Group()
archer = Archer(x, y)
moving_sprites_archer.add(archer)

# Creating an Infinite loop
run = True
while run:
    key_pressed_is = pygame.key.get_pressed()

    if game_paused == False:
        window.fill((155, 155, 155))
        font = pygame.font.SysFont(None, 30)
        img = font.render('Lives =', True, (0, 10, 90))
        screen.blit(img, (50, 50))
        img = font.render(str(lifes1), 1, (0, 10, 90))
        screen.blit(img, (130, 50))
        img = font.render('Lives =', True, (150, 0, 150))
        screen.blit(img, (650, 50))
        img = font.render(str(lifes2), 1, (150, 0, 150))
        screen.blit(img, (730, 50))
        # Set the frame rates to 60 fps
        clock.tick(60)
        pygame.draw.line(window, (100, 100, 250), (0, 500), (1000, 500), 75)
        if lifes2 == 0:
            window.fill((155, 0, 155))
            font = pygame.font.SysFont(None, 30)
            img = font.render('The winner is the purple player', True, (150, 0, 150))
            screen.blit(img, (250, 50))
            if key_pressed_is[K_l]:
                lifes1 += 3
        if lifes1 == 0:
            window.fill((0, 155, 0))
            font = pygame.font.SysFont(None, 30)
            img = font.render('The winner is the green player', True, (150, 0, 150))
            screen.blit(img, (250, 50))
        elif (lifes1 != 0) and (lifes2 != 0):
            if jump == False:
                # if space bar is pressed
                if key_pressed_is[pygame.K_SPACE]:
                    # make is jump equal to True
                    jump = True
            if jump:
                # calculate force (F). F = 1 / 2 * mass * velocity ^ 2.
                Force = (1 / 4) * mass * (vel ** 2)
                # change in the y co-ordinate
                y -= Force
                # decreasing velocity while going up and become negative while coming down
                vel = vel - 1

                # object reached its maximum height
                if vel < 0:
                    # negative sign is added to counter negative velocity
                    mass = -1
                # objected reaches its original state
                if vel == -10:
                    # making is jump equal to false
                    jump = False
                    vel = 9
                    mass = 1

            if jump1 == False:
                # if space bar is pressed
                if key_pressed_is[pygame.K_z]:
                    # make is jump equal to True
                    jump1 = True
            if jump1:
                # calculate force (F). F = 1 / 2 * mass * velocity ^ 2.
                Force1 = (1 / 4) * mass1 * (vel1 ** 2)
                # change in the y co-ordinate
                y1 -= Force1
                # decreasing velocity while going up and become negative while coming down
                vel1 = vel1 - 1

                # object reached its maximum height
                if vel1 < 0:
                    # negative sign is added to counter negative velocity
                    mass1 = -1
                # objected reaches its original state
                if vel1 == -11:
                    jump1 = False
                    vel1 = 10
                    mass1 = 1

            if direction:
                window.blit(pygame.transform.flip(image, True, False), (x, y))
            if not direction:
                window.blit(image, (x, y))

            if not directionArrow:
                window.blit(pygame.transform.flip(shoot, True, False), (xb1, yb1))
            if directionArrow:
                window.blit(shoot, (xb1, yb1))

            if not direction2:
                window.blit(pygame.transform.flip(image2, True, False), (x1, y1))
            if direction2:
                window.blit(image2, (x1, y1))
            if not directionArrow2:
                window.blit(pygame.transform.flip(shoot1, True, False), (xb, yb))
            if directionArrow2:
                window.blit(shoot1, (xb, yb))




            if (x - 26 < xb < x + 26) and (y - 40 < yb < y + 40):
                lifes1 -= 1
                xb = -800
                yb = -800
            if (x1 - 12 < xb1 < x1 + 12) and (y1 - 10 < yb1 < y1 + 10):
                lifes2 -= 1
                xb1 = -800
                yb1 = -800
            # iterate over the list of Event objects
            # that was returned by pygame.event.get() method.
            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_paused = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE and (menu_state == "key" or menu_state == 'audio'):
                        menu_state = "options"
                    if event.key == pygame.K_m:
                        if music:
                            # Pause the music
                            mixer.music.pause()
                            music = False
                        else:
                            mixer.music.unpause()
                            music = True
                    if event.key == pygame.K_t:
                        pygame.mixer.music.set_volume(volume - 0.1)
                        volume -= 0.1
                    if event.key == pygame.K_y:
                        pygame.mixer.music.set_volume(volume + 0.1)
                        volume += 0.1

            # Closing the window and program if the
            # type of the event is QUIT
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

        # Storing the key pressed in a
        # new variable using key.get_pressed()
        # method

        # Changing the coordinates
        # of the player
        if key_pressed_is[K_q]:
            direction2 = True
            x1 -= 3
            if x1 < -20:
                x1 = 740
        if key_pressed_is[K_d]:
            direction2 = False
            x1 += 3
            if x1 > 740:
                x1 = -20
        if key_pressed_is[K_LEFT]:
            x -= 3
            if x < -20:
                x = 740
            direction = False
        if key_pressed_is[K_RIGHT]:
            x += 3
            if x > 740:
                x = -20
            direction = True
        if key_pressed_is[K_s]:
            xb = x1
            xp1 = xb
            yb = y1
            yp1 = yb
            if direction2:
                directionArrow2 = True
            else:
                directionArrow2 = False
            Fire = True
        else:
            KeyTime = False
        if key_pressed_is[K_p]:
            xb1 = x
            xp = x
            yb1 = y
            yp = y
            if direction:
                directionArrow = True
            else:
                directionArrow = False
            Fire1 = True
        if Fire:
                if directionArrow2:
                    A1=90
                    Time2 += 0.05
                    VitesseI = 70
                    Angle = -230
                    g = 18
                    xb = xp1 + (VitesseI * math.cos(Angle) * Time2)
                    yb = yp1 + (1 / 2) * g * Time2 * Time2 - VitesseI * math.sin(Angle) * Time2
                if not directionArrow2:
                    Time2 += 0.05
                    VitesseI = 70
                    Angle = -230
                    g = 18
                    xb = xp1 - (VitesseI * math.cos(Angle) * Time2)
                    yb = yp1 + (1 / 2) * g * Time2 * Time2 - VitesseI * math.sin(Angle) * Time2
        if not Fire:
            Time2 = 0
            xb = 0
            yb = 0
        if Fire1:
            if directionArrow:

                Time += 0.05
                VitesseI = 70
                Angle = -230
                g = 18
                xb1 = xp - (VitesseI * math.cos(Angle) * Time)
                yb1 = yp + (1 / 2) * g * Time * Time - VitesseI * math.sin(Angle) * Time
            if not directionArrow:
                Time += 0.05
                VitesseI = 70
                Angle = -230
                g = 18
                xb1 = xp + (VitesseI * math.cos(Angle) * Time)
                yb1 = yp + (1 / 2) * g * Time * Time - VitesseI * math.sin(Angle) * Time
        if not Fire1:
            Time = 0
            xb1=0
            yb1=0
        if xb < -30 or xb > 730:
            Fire = False
            xb = 800
        if yb < 350 or yb > 600:
            Fire = False
            yb = 800
        if xb1 < 0 or xb1 > 730:
            Fire1 = False
            xb1 = 800
        if yb1 < 50 or yb1 > 800:
            Fire1 = False
            yb1 = 800
        # Draws the surface
        # object to the screen.
    pygame.display.update()
