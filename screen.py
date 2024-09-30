import pygame

pygame.init()

screen = pygame.display.set_mode((800, 700))

pygame.display.set_caption('Geeks for geeks')

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

