import pygame
from spot import *
from colors import *

#A CLASS TO REPRESENT THE GRID OF THE VISUALIZER. 
class Grid: 
    
    #GRID CONSTRUCTOR
    def __init__(self, rows, size): 
        #initialize the instance variables for the grid object.
        self.grid = []
        self.gap = size//rows #the gap between each row -- the gap within each square cell. 
        self.rows = rows
        self.size = size 

        #create the actual grid by populating a two-dimensional list with Spots.
        for i in range(self.rows):  
            row = []
            for j in range(self.rows): 
                row.append(Spot(i, j, self.gap, self.rows))
            self.grid.append(row)

    #GRID DRAWING METHOD
    def draw_grid(self, surface): 

        #fill the surface with a white overlay.
        surface.fill(WHITE)

        #drawing the individual spots -- these will seem invisible, as the grid is white colored originally.
        for row in self.grid: 
            for spot in row: 
                spot.draw(surface)

        #drawing the lines of the grid -- the seperators that actually define the grid.
        #note. we are drawing horizontal lines along the vertical axis first. 
        for i in range(self.rows): 
            pygame.draw.line(surface, GREY, (0, i*self.gap), (self.size, i*self.gap))
        
        #then, we are drawing the vertical lines along the horizontal axis.
        for j in range(self.rows): 
           pygame.draw.line(surface, GREY, (j*self.gap, 0), (j*self.gap, self.size))

        pygame.display.update()
    
