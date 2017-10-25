import os
import random
import numpy
import pygame

from Map_Matrix import *

"""This is dealing with making and ensuring the map will be random"""


def generate_random_map():
    # Position X and Y on the game window
    pos_x = 0
    pos_y = 0
    rules_for_tiles()

    # for loop that blits to the screen each tile number within the modified ruled matrix.
    for row_num, row_list in enumerate(map_matrix):
        for tile_num in enumerate(row_list):
            load_tile = pygame.image.load(list_of_tiles[tile_num[1]])
            game_window.blit(load_tile, (pos_x, pos_y))

            pos_x += 64
        pos_y += 64
        pos_x = 0

    # this will print the matrix in the console.
    print map_matrix


# Generates a random map with a set of rules for paths to stay aligned.
generate_random_map()