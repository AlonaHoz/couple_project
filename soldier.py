import game_field
import pygame
import consts

keys = pygame.key.get_pressed()
while not keys[pygame.K_ESCAPE]:
    move = "nothing yet"
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        consts.Y -= 1
        move = "up"
    elif keys[pygame.K_DOWN]:
        consts.Y += 1
        move = "down"
    elif keys[pygame.K_LEFT]:
        consts.X -= 1
        move = "left"
    elif keys[pygame.K_RIGHT]:
        consts.X += 1
        move = "right"


def result_of_move():
    if move == "up":


