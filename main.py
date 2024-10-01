import time

import pygame
import screen
import soldier

soldier_loc = [0, 0]
cube = 20

running = True
while running:
    key_pressed = pygame.key.get_pressed()
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        screen.print_normal()
        if key_pressed[pygame.K_RETURN]:
            screen.black_screen()
            time.sleep(1)
            screen.print_normal()












