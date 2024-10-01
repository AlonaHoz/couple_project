import time

import pygame
import screen
import soldier

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        screen.print_normal()
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RETURN]:
            screen.black_screen()
            time.sleep(1)
            screen.print_normal()
            soldier.move_soldier()










