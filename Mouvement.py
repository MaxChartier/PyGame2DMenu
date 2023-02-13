# Importing pygame module
import pygame
from pygame.locals import *
import button
from pygame import mixer

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

# create game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

# game variables
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
image = pygame.image.load(r'Images/Player_image.png')
image2 = pygame.image.load(r'Images/Player_image1.png')
fire1 = pygame.image.load(r'Images/ball1.png')
# Store the initial
# coordinates of the player in
# two variables i.e. x and y.
x1 = 600
y1 = 396
x = 150
y = 396
xb = -800
yb = -800

# Create a variable to store the
# velocity of player's movement
velocity = 1
vel = 9
mass = 1
vel1 = 10
mass1 = 1

# Creating an Infinite loop
run = True
while run:
    key_pressed_is = pygame.key.get_pressed()

    if game_paused:
        # check menu state
        if menu_state == "main":
            screen.fill((0, 0, 0))
            # draw pause screen buttons
            if resume_button.draw(screen):
                game_paused = False
            if options_button.draw(screen):
                screen.fill((0, 0, 0))
                menu_state = "options"
            if quit_button.draw(screen):
                run = False
        # check if the options menu is open
        if menu_state == "options":
            # draw the different options buttons
            if audio_button.draw(screen):
                menu_state = "audio"
            if keys_button.draw(screen):
                menu_state = 'key'
            if back_button.draw(screen):
                menu_state = "main"
        if menu_state == 'key':
            font = pygame.font.SysFont(None, 30)
            img = font.render('- To move your character use the arrows', True, (255, 255, 255))
            screen.blit(img, ((SCREEN_WIDTH / 2) - 220, SCREEN_HEIGHT / 8))
            img = font.render('- To increase the music press Y', True, (255, 255, 255))
            screen.blit(img, ((SCREEN_WIDTH / 2) - 220, 2 * SCREEN_HEIGHT / 8))
            img = font.render('- To decrease the music press T', True, (255, 255, 255))
            screen.blit(img, ((SCREEN_WIDTH / 2) - 220, 3 * SCREEN_HEIGHT / 8))
            img = font.render('- To pause the music press M', True, (255, 255, 255))
            screen.blit(img, ((SCREEN_WIDTH / 2) - 220, 4 * SCREEN_HEIGHT / 8))
            font = pygame.font.SysFont(None, 20)
            img = font.render('Press esc to go back to the settings', True, (255, 255, 255))
            screen.blit(img, (10, 10))
        if menu_state == "audio":
            screen.fill((0, 0, 0))
            font = pygame.font.SysFont(None, 30)
            img = font.render('Choose the music you want to play with : ', True, (255, 255, 255))
            screen.blit(img, (200, 100))
            font = pygame.font.SysFont(None, 20)
            img = font.render('Press esc to go back to the settings', True, (255, 255, 255))
            screen.blit(img, (10, 10))
    if game_paused == False:
        window.fill((0, 0, 0))
        font = pygame.font.SysFont(None, 30)
        img = font.render('Lives =', True, (150, 0, 150))
        screen.blit(img, (50, 50))
        img = font.render(str(lifes1), 1, (150, 0, 150))
        screen.blit(img, (130, 50))
        img = font.render('Lives =', True, (0, 150, 0))
        screen.blit(img, (650, 50))
        img = font.render(str(lifes1), 1, (0, 150, 0))
        screen.blit(img, (730, 50))
        # Set the frame rates to 60 fps
        clock.tick(60)
        pygame.draw.line(window, (100, 100, 250), (0, 500), (1000, 500), 75)
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
                # making isjump equal to false
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

        # Filling the background with
        # white color
        if direction == True:
            window.blit(image, (x, y))
        if direction == False:
            window.blit(pygame.transform.flip(image, True, False), (x, y))

        # Display the player sprite at x
        # and y coordinates
        window.blit(fire1, (xb, yb))
        window.blit(image, (x, y))
        window.blit(image2, (x1, y1))
        if (x - 25 < xb < x + 25) and (y - 25 < yb < y + 25):
            lifes1 -= 1
            xb = -800
            yb = -800
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

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            direction = True
        elif event.key == pygame.K_LEFT:
            direction = False

    # Storing the key pressed in a
    # new variable using key.get_pressed()
    # method

    # Changing the coordinates
    # of the player
    if key_pressed_is[K_q]:
        x1 -= 3
        if x1 < -20:
            x1 = 740
    if key_pressed_is[K_d]:
        x1 += 3
        if x1 > 740:
            x1 = -20
    if key_pressed_is[K_LEFT]:
        x -= 3
        if x < -20:
            x = 740
    if key_pressed_is[K_RIGHT]:
        x += 3
        if x > 740:
            x = -20
    if key_pressed_is[K_s]:
        xb = x1
        yb = y1
        Fire = True
    if Fire:
        xb -= 4
        yb += 0.3
    if (xb < -30 or xb > 730):
        Fire = False
        xb = 800
    if (yb < 350 or yb > 600):
        Fire = False
        yb = 800
    # Draws the surface
    # object to the screen.
    pygame.display.update()
