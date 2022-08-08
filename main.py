import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import math
import colors
from spot import *
from a_star import *

#setting up the display window width, dimensions, and caption (title). 
WIDTH = 800
WINDOW = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("PathFinding Visualizer.")

#MAKE GRID
def make_grid(rows, width): 
    grid = [] #represents the grid as a list. 
    gap = width // rows #represents the width of each square/spot. 
    
    for i in range(rows): 






if __name__ == "__main__": 
    pass
