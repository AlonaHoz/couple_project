import pygame

import game_field
from game_field import create_board
from game_field import put_mine


pygame.init()


screen = pygame.display.set_mode((1000, 500))

pygame.display.set_caption('The Flag')

green = (0, 50, 0)
black = (0, 0, 0,)

put_mine()

grid_node_width = 20
grid_node_height = 20


def create_square(z, y, color):
    pygame.draw.rect(screen, color, [z, y, grid_node_width, grid_node_height])


def visualize_grid():
    y = 0
    for row in create_board():
        z = 0
        for item in row:
            if item == 20:
                create_square(z, y, green)
            else:
                create_square(z, y, green)

            z += grid_node_width
        y += grid_node_height
    pygame.display.update()


visualize_grid()

board = game_field.put_bush()
for i in range(25):
    for j in range(50):
        if "second" in board[i][j]:
            img = pygame.image.load('grass.png')
            img = pygame.transform.scale(img, (60, 60))
            screen.blit(img, (j * 18, i * 18))
            pygame.display.flip()
        if "fourth" in board[i][j]:
            img = pygame.image.load('soldier.png')
            img = pygame.transform.scale(img, (60, 60))
            screen.blit(img, (j * 20, i * 20))
            pygame.display.flip()
        if "third" in board[i][j]:
            img = pygame.image.load('flag.png')
            img = pygame.transform.scale(img, (60, 60))
            screen.blit(img, (j * 20, i * 20))
            pygame.display.flip()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            screen.fill(black)
            for x in range(0, 1000, 20):
                pygame.draw.line(screen, green, (1, x), (1000, x), 2)
                pygame.draw.line(screen, green, (x, 1), (x, 1000), 2)
                pygame.display.update()
            board = game_field.put_bush()
            for i in range(25):
                for j in range(50):
                    if "first" in board[i][j]:
                        img = pygame.image.load('mine.png')
                        img = pygame.transform.scale(img, (60, 20))
                        screen.blit(img, (j*20, i*20))
                        pygame.display.flip()


