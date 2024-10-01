import game_field
import pygame
import game_field
import consts
import screen


def move_soldier():
    board = game_field.put_bush()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                for i in range(25):
                    for j in range(50):
                        if board[i][j] == "fourth body":
                            board[i][j] = "FREE"
                            board[i - 1][j] = "fourth body"
                        elif board[i][j] == "body":
                            board[i][j] = "FREE"
                            board[i - 1][j] = "body"
                        elif board[i][j] == "leg":
                            board[i][j] = "FREE"
                            board[i - 1][j] = "leg"
                    pygame.display.update()
            elif event.key == pygame.K_DOWN:
                for i in range(25):
                    for j in range(50):
                        if board[i][j] == "fourth body":
                            board[i][j] = "FREE"
                            board[i + 1][j] = "fourth body"
                        elif board[i][j] == "body":
                            board[i][j] = "FREE"
                            board[i + 1][j] = "body"
                        elif board[i][j] == "leg":
                            board[i][j] = "FREE"
                            board[i + 1][j] = "leg"
                pygame.display.update()
            elif event.key == pygame.K_LEFT:
                for i in range(25):
                    for j in range(50):
                        if board[i][j] == "fourth body":
                            board[i][j] = "FREE"
                            board[i][j - 1] = "fourth body"
                        elif board[i][j] == "body":
                            board[i][j] = "FREE"
                            board[i][j - 1] = "body"
                        elif board[i][j] == "leg":
                            board[i][j] = "FREE"
                            board[i][j - 1] = "leg"
                pygame.display.update()
            elif event.key == pygame.K_RIGHT:
                for i in range(25):
                    for j in range(50):
                        if board[i][j] == "fourth body":
                            board[i][j] = "FREE"
                            board[i][j + 1] = "fourth body"
                        elif board[i][j] == "body":
                            board[i][j] = "FREE"
                            board[i][j + 1] = "body"
                        elif board[i][j] == "leg":
                            board[i][j] = "FREE"
                            board[i][j + 1] = "leg"
                pygame.display.update()
        return board


