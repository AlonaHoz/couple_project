import time

import pygame
import screen

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


screen.print_normal()
screen.black_screen()
screen.print_normal()
pygame.time.delay(10000)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False




