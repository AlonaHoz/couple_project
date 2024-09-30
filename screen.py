import pygame
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
            if item == 0:
                create_square(z, y, (255, 255, 255))
            else:
                create_square(z, y, green)

            z += grid_node_width
        y += grid_node_height
    pygame.display.update()


visualize_grid()

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

scorn = pygame.display.set_mode((500, 400))

# set the pygame window name
pygame.display.set_caption('image')

# create a surface object, image is drawn on it.
imp = pygame.image.load("C:\\Users\\DELL\\Downloads\\gfg.png").convert()

# Using blit to copy content from one surface to other
scrn.blit(imp, (0, 0))

