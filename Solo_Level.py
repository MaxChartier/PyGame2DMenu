# Importing pygame module
import random
from pygame.locals import *
import pygame.display
import math

screen = pygame.display.set_mode((800, 600))

# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()
# create the display surface object
# of specific dimension.
pygame.display.set_caption("Arcane Archer")

# game variables
Game_over = False
game_paused = False
menu_state = "main"
lifes = 3
score = 0

# define fonts
font = pygame.font.SysFont("arial black", 40)

# define colours
TEXT_COL = (255, 255, 255)


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


# creating actions
direction = True
jump = False
v_new = 5
m_new = 1
Time = 0

# Add caption in the window
pygame.display.set_caption('Player Movement')

# Initializing the clock
# Clocks are used to track and
# control the frame-rate of a game
clock = pygame.time.Clock()

# Add player sprite
image = pygame.image.load(r"Images/Player_image1.gif")
image = pygame.transform.scale(image, (66, 90))
pv_image = pygame.image.load("Images/PV/1_life.png")
background_image = pygame.image.load("Images/background_for_game.jpg")
arrow_image = pygame.image.load("Images/ball2.png")
zombie_image = pygame.image.load("Images/zombie.png")
zombie_image = pygame.transform.scale(zombie_image, (66, 90))
zombie_x = 600
zombie_y = 450

# Store the initial
# coordinates of the player in
# two variables i.e. x and y.
x = 50
y = 450

walking = False
walking_steps = 0
player_current = 0
arrow_x = x
arrow_y = y
arrow_speed = 5
arrow_angle = 0
arrow_fired = False
arrow_velocity_x = 0
arrow_velocity_y = 0
gravity = 0.1  # set gravity
shot_strength = 0.8  # set initial shot strength
shot_strength_scale = 3.2  # set shot strength scale

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
    if lifes==1:
        pv_image == pygame.image.load("Images/PV/1_life.png")
    if lifes== 2:
        pv_image == pygame.image.load("Images/PV/2_lifes.png")
    if lifes == 3:
        pv_image == pygame.image.load("Images/PV/3_lifes.jpg")
    key_pressed_is = pygame.key.get_pressed()
    if not game_paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and not arrow_fired:
                arrow_fired = True
                arrow_x = x
                arrow_y = y
                mouse_x, mouse_y = pygame.mouse.get_pos()
                arrow_angle = math.atan2(y + 25 - mouse_y, x + 50 - mouse_x)
                arrow_velocity_x = -arrow_speed * math.cos(arrow_angle) * shot_strength
                arrow_velocity_y = -arrow_speed * math.sin(arrow_angle) * shot_strength
                shot_strength = 0.8
            elif event.type == pygame.KEYDOWN and not arrow_fired and event.key == pygame.K_l:
                shot_strength = min(2.0, shot_strength + 0.4)
        # Set the frame rates to 60 fps
        clock.tick(60)
        if lifes != 0:
            if not jump:
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

            # iterate over the list of Event objects
            # that was returned by pygame.event.get() method.
        # of the player
        if key_pressed_is[K_q]:
            x -= 3
            if x < -20:
                x = 740
                if map == 2:
                    map = 1
            direction = False
        if key_pressed_is[K_d]:
            x += 3
            direction = True
            if x > 740:
                x = -20
                screen.fill((255, 255, 255))

    if arrow_fired:
        arrow_x += arrow_velocity_x
        arrow_y += arrow_velocity_y
        arrow_velocity_y += gravity

    if arrow_fired:
        if (zombie_x - 30 < arrow_x < zombie_x + 30) and (zombie_y - 20 < arrow_y < zombie_y + 40):
            score +=10
            arrow_fired = False
            zombie_x = random.randint(0, 600)
            if (x + 40 >= zombie_x >= x - 40):
                zombie_x = random.randint(0, 600)
            if zombie_x > x:
                zombie_image = (pygame.transform.flip(zombie_image, True, False))
            else:
                zombie_image = zombie_image
    if (x+20 >= zombie_x >= x-20):
        lifes -= 1;
        zombie_x = random.randint(0, 600)
        if (x+40 >= zombie_x >= x-40):
            zombie_x = random.randint(0, 600)
    if zombie_x > x:
        zombie_x -= score/200
    else:
        zombie_x += score/200

        # Check for collisions with ground
    if arrow_y + arrow_image.get_height() > 750:
        arrow_fired = False
        arrow_velocity_x = 0
        arrow_velocity_y = 0

    if direction:
        screen.blit(background_image, (0, 0))
        screen.blit(pygame.transform.flip(image, True, False), (x, y))
    if not direction:
        screen.blit(background_image, (0, 0))
        screen.blit(image, (x, y))

    screen.blit(zombie_image, (zombie_x, zombie_y))


    if arrow_y + arrow_image.get_height() > 550:
        arrow_fired = False
        arrow_velocity_x = 0
        arrow_velocity_y = 0

    # Draw arrow if fired
    if arrow_fired:
        screen.blit(pygame.transform.rotate(arrow_image, math.degrees(-arrow_angle)), (arrow_x, arrow_y))
        if x<arrow_x:
            arrow_angle += shot_strength/60
        if x>arrow_x:
            arrow_angle -= shot_strength/60
    # Draw shot strength meter
    pygame.draw.rect(screen, (255, 255, 255), (25, 25, 10, 100))
    meter_height = int(shot_strength / shot_strength_scale * 160)
    pygame.draw.rect(screen, (181, 154, 84), (25, 125 - meter_height, 10, meter_height))

    font = pygame.font.SysFont(None, 30)
    img = font.render('Lives =', True, (0, 10, 90))
    screen.blit(img, (50, 50))
    img = font.render(str(lifes), 1, (0, 10, 90))
    screen.blit(img, (130, 50))
    img = font.render('score =', True, (0, 30, 90))
    screen.blit(img, (50, 80))
    img = font.render(str(score), 1, (0, 10, 90))
    screen.blit(img, (130, 80))
    # Update screen
    pygame.display.flip()
    if lifes == 0:
        print("You lost!")

# Quit Pygame
pygame.quit()
