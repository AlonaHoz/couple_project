import game_field
import pygame
import game_field
import consts
import screen


def move_soldier():
    board = game_field.put_bush()
    key = pygame.key.get_pressed()
    if key[pygame.K_UP]:
        for i in range(25):
            for j in range(50):
                if board[i][j] == "fourth body":
                    board[i][j] = "FREE"
                    board[i - 20][j] = "fourth body"
                elif board[i][j] == "body":
                    board[i][j] = "FREE"
                    board[i - 20][j] = "body"
                elif board[i][j] == "leg":
                    board[i][j] = "FREE"
                    board[i - 20][j] = "leg"
    elif key[pygame.K_DOWN]:
        for i in range(25):
            for j in range(50):
                if board[i][j] == "fourth body":
                    board[i][j] = "FREE"
                    board[i + 20][j] = "fourth body"
                elif board[i][j] == "body":
                    board[i][j] = "FREE"
                    board[i + 20][j] = "body"
                elif board[i][j] == "leg":
                    board[i][j] = "FREE"
                    board[i + 20][j] = "leg"
    elif key[pygame.K_LEFT]:
        for i in range(25):
            for j in range(50):
                if board[i][j] == "fourth body":
                    board[i][j] = "FREE"
                    board[i][j - 20] = "fourth body"
                elif board[i][j] == "body":
                    board[i][j] = "FREE"
                    board[i][j - 20] = "body"
                elif board[i][j] == "leg":
                    board[i][j] = "FREE"
                    board[i][j - 1] = "leg"
    elif key[pygame.K_RIGHT]:
        for i in range(25):
            for j in range(50):
                if board[i][j] == "fourth body":
                    board[i][j] = "FREE"
                    board[i][j + 20] = "fourth body"
                elif board[i][j] == "body":
                    board[i][j] = "FREE"
                    board[i][j + 20] = "body"
                elif board[i][j] == "leg":
                    board[i][j] = "FREE"
                    board[i][j + 20] = "leg"
    return board





