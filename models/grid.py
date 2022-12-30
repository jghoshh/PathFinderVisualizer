import pygame
from models.spot import *
from constants.colors import *

#A CLASS TO REPRESENT THE GRID OF THE VISUALIZER. 
class Grid: 

    
    #GRID CONSTRUCTOR
    def __init__(self, rows, size): 
        #initialize the instance variables for the grid object.
        self.grid = []
        self.gap = size//rows #the gap between each row -- the gap within each square cell. 
        self.rows = rows
        self.size = size #size represents the length and width of the pygame UI window.

        #create the actual grid by populating a two-dimensional list with Spots.
        for i in range(self.rows):  
            row = []
            for j in range(self.rows): 
                row.append(Spot(i, j, self.gap, self.rows))
            self.grid.append(row)


    #GRID DRAWING METHOD
    def draw_grid(self, surface): 

        #drawing the individual spots with the base color of white.
        for row in self.grid: 
            for spot in row: 
                spot.draw_spot(surface)

        #drawing the lines of the grid -- the seperators that make the grid look like a grid.
        #note. we are drawing horizontal lines along the vertical axis first. 
        for i in range(self.rows): 
            pygame.draw.line(surface, BLACK, (0, i*self.gap), (self.size, i*self.gap))
        
        #then, we are drawing the vertical lines along the horizontal axis.
        for j in range(self.rows): 
           pygame.draw.line(surface, BLACK, (j*self.gap, 0), (j*self.gap, self.size))

        pygame.display.update()
    
