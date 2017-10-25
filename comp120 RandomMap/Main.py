import os
import random
import numpy
import pygame

""" This is getting information from Random_Map """
from Random_Map import*


"""
New map generator, this one works by using a matrix to define
where it should place the tiles on the game window.
"""

# The game window while loop.
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    # blits random tiles to the game window on mouse click down.
    if event.type == pygame.MOUSEBUTTONDOWN:
        generate_random_map()

    pygame.display.flip()
