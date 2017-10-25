import os
import random
import numpy
import pygame

"""This makes the game window to size required"""
# Variables to set the width and height of the game window.
game_window_width = 64 * 20
game_window_height = 64 * 12

# The game window itself.
game_window = pygame.display.set_mode((game_window_width, game_window_height))


""" This creates a random map matrix using the numpy array library."""
map_matrix = numpy.random.randint(11, size=(game_window_height / 64, game_window_width / 64))
