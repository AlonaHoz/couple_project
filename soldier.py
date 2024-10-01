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
                    board[i - 1][j] = "fourth body"
                elif board[i][j] == "body":
                    board[i][j] = "FREE"
                    board[i - 1][j] = "body"
                elif board[i][j] == "leg":
                    board[i][j] = "FREE"
                    board[i - 1][j] = "leg"
    elif key[pygame.K_DOWN]:
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
    elif key[pygame.K_LEFT]:
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
    elif key[pygame.K_RIGHT]:
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


def move_soldier_2():
    man_list = []
    board = game_field.put_mine()
    for i in range(25):
        for j in range(50):
            if board[i][j] == "fourth body" or "body" or "leg":
                man = (i, j)
                man_list.append(man)
    return man_list


