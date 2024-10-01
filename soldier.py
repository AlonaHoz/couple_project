import game_field
import pygame
import game_field
import consts

keys = pygame.key.get_pressed()
while not keys[pygame.K_ESCAPE]:
    board = game_field.put_bush()
    x = 0
    y = 0
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        for i in range(25):
            for j in range(50):
                if board[i][j] == "fourth body":
                    board[i][j] = "FREE"
                    board[i-1][j] = "fourth body"
    elif keys[pygame.K_DOWN]:
        y += 1
        move = (x, y)
    elif keys[pygame.K_LEFT]:
        x -= 1
        move = (x, y)
    elif keys[pygame.K_RIGHT]:
        x += 1
        move = (x, y)


def result_of_move():
    for