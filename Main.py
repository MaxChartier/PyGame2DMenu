import pygame
import button
from pygame import mixer

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
music1_img = pygame.image.load('Images/Music1.png')

# create button instances
resume_button = button.Button(304, 125, resume_img, 1)
options_button = button.Button(297, 250, options_img, 1)
quit_button = button.Button(336, 375, quit_img, 1)
video_button = button.Button(226, 75, video_img, 1)
audio_button = button.Button(225, 150, audio_img, 1)
keys_button = button.Button(246, 295, keys_img, 1)
back_button = button.Button(332, 430, back_img, 1)
music1_button = button.Button(304, 125, music1_img, 1)


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


# game loop
run = True
while run:
    screen.fill((0, 0, 0))

    # check if game is paused
    if game_paused:
        # check menu state
        if menu_state == "main":
            # draw pause screen buttons
            if resume_button.draw(screen):
                game_paused = False
            if options_button.draw(screen):
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
            font = pygame.font.SysFont(None, 30)
            img = font.render('Choose the music you want to play with : ', True, (255, 255, 255))
            screen.blit(img, (200, 100))
            font = pygame.font.SysFont(None, 20)
            img = font.render('Press esc to go back to the settings', True, (255, 255, 255))
            screen.blit(img, (10, 10))
            if music1_button.draw(screen):
                game_paused = False
    else:
        draw_text("Press Echap to pause", font, TEXT_COL, 160, 250)

    # event handler
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
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
