import pygame
from colors import *

#defining the spot class -- this class represents the fundamental building block of the visualizer.

class Spot: 
    def __init__(self, row, col, width, total_rows): 
        self.row = row #which row this spot is located in. 
        self.col = col #which column this spot is located in. 
        self.width = width #how wide this spot is (all spots will have the same width). 
        self.x = col*width #x-coordinate of the spot. 
        self.y = row*width #y-coordinate of the spot. 
        self.color = WHITE #base color of the spot. 
        self.neighbors = [] #neighbors of the spot -- to be utilized in the path finding algorithm. 
        self.rows = total_rows #if at anytime we need the total # of rows/coloums in the grid, we call this. 
        
    def get_pos(self): 
        return self.row, self.col #returning position in matrix indexing format. 
    
    #BOOLEAN CHECKS OF STATE // GETTERS
    #check if the spot has already been processed and checked during the algorithm: 
    def checked(self): 
        return self.color == RED 
    
    def not_checked(self): 
        return self.color == GREEN & self.color != BLACK 
    
    #check if the spot is a barrier:  
    def is_barrier(self): 
        return self.color == BLACK 
    
    #check if the spot is the start node:  
    def is_start(self): 
        return self.color == ORANGE
    
    #check if the spot is the end node: 
    def is_end(self): 
        return self.color == PURPLE
    
    #ENFORCING METHODS // SETTERS
    
    #reset the color of the spot to assign it a specific role: 
    def reset(self): 
        self.color = WHITE
    
    def make_closed(self): 
        self.color = RED
    
    def make_open(self): 
        self.color = GREEN
        
    def make_barrier(self): 
        self.color = BLACK
        
    def make_end(self): 
        self.color = PURPLE
        
    def make_start(self): 
        self.color = ORANGE
    
    def make_path(self): 
        self.color = TURQUOISE
          
    #DRAW THE SPOTS
    def draw(self, window): 
        #drawing the rectangle spot -- rectangle parameter is represented as a tuple of coordinates, width, and height. 
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.width))
    
    #UPDATE NEIGHBORS
    def update_neighbors(self, grid): 
        pass
        
    #LESS THAN FUNCTION
    def __lt__(self, other): 
        return False