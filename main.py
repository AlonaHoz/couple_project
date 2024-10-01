import time

import pygame
import screen
import soldier
key = pygame.key.get_pressed()


running = True
while running:
    screen.print_normal()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if key == pygame.K_RETURN:
            screen.black_screen()
            time.sleep(1)

        soldier.move_soldier()
        screen.print_normal()










