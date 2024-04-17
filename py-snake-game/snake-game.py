# TODO: Thinking the architeture of game

# How it works the snake game?
# First, we have the screen. (x: 600, y:600)
# The snake "eats" the points with its head


# libs
import pygame
import time
import random

snake_speed = 15

# size
window_x = 600
window_y = 600

# colors (rgb format)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

pygame.init()

pygame.display.set_caption('Snake Game')
game_window = pygame.display.set_mode((window_x, window_y))

fps = pygame.time.Clock()


snake_default_pos = [100, 100]
snake_body = [[100, 100],
              [90, 100],
              [80, 100],
              [70, 100]]

fruit_pos = [random.randrange(1, (window_x//10)) * 10,
             random.randrange(1, (window_y//10)) * 10]

fruit_spawn = True

snake_direction = 'RIGHT'
change_to = snake_direction


# Function to display the score

score = 0

def display_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)

    score_surface = score_font.render('Score: ' + str(score), True, color)

    score_rect = score_surface.get_rect()

    game_window.blit(score_surface, score_rect)


# Function to game over ()

def game_over():
    game_over_font = pygame.font.SysFont('times new roman', 50)

    game_over_surface = game_over_font.render('Your score is: ' +  str(score))

    game_over_rect = game_over_surface.get_rect()

    game_over_rect.midtop = (window_x/2, window_y/4)

    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    time.sleep(2)

    pygame.quit()

    quit()


# Main function

while True:

    # Key events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

