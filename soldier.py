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


soldier_loc = [0, 0]
cube = 20


def move_soldier_2():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.KEY == pygame.K_UP:
                soldier_loc[0] -= cube
            elif event.KEY == pygame.K_DOWN:
                soldier_loc[0] -= cube
            elif event.KEY == pygame.K_LEFT:
                soldier_loc[1] -= cube
            elif event.KEY == pygame.K_RIGHT:
                soldier_loc[1] += cube
    img = pygame.image.load('soldier.png')
    img = pygame.transform.scale(img, (60, 60))
    screen.screen.blit(img, (soldier_loc[0] * 20, soldier_loc[1] * 20))
    pygame.display.update()




