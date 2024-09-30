import pygame

pygame.init()

screen = pygame.display.set_mode((1000, 500))

pygame.display.set_caption('The Flag')

green = (0, 50, 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for x in range(0, 1000, 20):
        pygame.draw.line(screen,green,(1,x), (1000, x),2)
        pygame.draw.line(screen, green, (x, 1), (x, 1000), 2)
        pygame.display.update()



