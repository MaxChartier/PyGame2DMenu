# Importing pygame module
import time

import pygame
from pygame.locals import *
import button
import pygame.display
import pytmx
import pyscroll

screen = pygame.display.set_mode((800,600))

# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

# create the display surface object
# of specific dimension.
window = pygame.display.set_mode((600, 600))

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
jump = False
v_new = 5
m_new = 1

# Add caption in the window
pygame.display.set_caption('Player Movement')

# Initializing the clock
# Clocks are used to track and
# control the frame-rate of a game
clock = pygame.time.Clock()

# Add player sprite
player_images = []
player_images.append( pygame.image.load(r'Images/Player_image1.gif') )
player_images.append( pygame.image.load('Images/Player_image1.2.png') )
image = pygame.image.load(r"Images/Player_image1.gif")
image = pygame.transform.scale(image, (66, 90))
walking = False
walking_steps = 0
player_current = 0
player = player_images[ player_current ]

if map == 1:
    window.fill((155,155,155))
    pygame.draw.line(window, (100, 100, 250), (0, 500), (1000, 500), 75)
if map == 2:
    window.fill((155,0,155))
    pygame.draw.line(window, (100, 100, 250), (0, 500), (1000, 500), 75)

# Store the initial
# coordinates of the player in
# two variables i.e. x and y.
x1 = 600
y1 = 420
x = 150
y = 420


# Create a variable to store the
# velocity of player's movement
velocity = 1
vel = 9
mass = 1
vel1 = 10
mass1 = 1


# Creating an Infinite loop
run = True
map = 1
while run:
    if walking == True:
        # here you need to check some counter
        # if it is time for next step to walk slower
        # but don't use `time.sleep()`
        if walking_steps > 0:
            player_current = (player_current + 1) % len(player_images)
            player = player_images[player_current]
            walking_steps -= 10
        else:
            walking = False
    key_pressed_is = pygame.key.get_pressed()
    if map == 1:
        window.fill((155, 155, 155))
        pygame.draw.line(window, (100, 100, 250), (0, 500), (1000, 500), 75)
    if map == 2:
        window.fill((155, 0, 155))
        pygame.draw.line(window, (100, 100, 250), (0, 500), (1000, 500), 75)
    if game_paused == False:
        font = pygame.font.SysFont(None, 30)
        img = font.render('Lives =', True, (0, 10, 90))
        screen.blit(img, (50, 50))
        img = font.render(str(lifes1), 1, (0, 10, 90))
        screen.blit(img, (130, 50))
        # Set the frame rates to 60 fps
        clock.tick(60)
        if (lifes1 != 0):
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


            if direction:
                window.blit(pygame.transform.flip(player, True, False), (x, y))
            if not direction:
                window.blit(player, (x, y))


            # iterate over the list of Event objects
            # that was returned by pygame.event.get() method.
            for event in pygame.event.get():
              if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

        # of the player
        if key_pressed_is[K_q]:
            x -= 3
            walking = True
            walking_steps = 5
            if x < -20:
                x = 740
                if map == 2:
                    map = 1
            direction = False
        if key_pressed_is[K_d]:
            x += 3
            if x > 740:
                x = -20
                window.fill((255, 255, 255))
                if map == 1:
                    map = 2


            direction = True


    pygame.display.update()
