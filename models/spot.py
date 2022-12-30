import pygame
from constants.colors import *

#A CLASS FOR THE FUNDAMENTAL BUILDING BLOCK OF THE VISUALIZER.
class Spot: 

    def __init__(self, row, col, width, total_rows): 
        self.row = row #which row this spot is located in. 
        self.col = col #which column this spot is located in. 
        self.width = width #how wide this spot is (all spots will have the same size). 
        self.x = col*width #x-coordinate of the spot -- the location of the spot in terms of pygame. 
        self.y = row*width #y-coordinate of the spot -- the location of the spot in terms of pygame.
        self.color = WHITE #base color of the spot. 
        self.neighbours = [] #neighbours of the spot -- to be utilized in the path finding algorithm
        self.rows = total_rows #if at anytime we need the total # of rows/columns in the square grid, we call this. 

    #CHECKS OF STATE // GETTERS
    #returns the position of the spot in the matrix of spots defining the path finding maze. 
    #note. we are indexing by row, col because we will be storing these spots in a matrix.  
    def get_pos(self):
        return self.row, self.col #returning position in matrix indexing format. 
    
    #check if the spot has already been processed or checked during the algorithm runtime.
    def is_visited(self): 
        return self.color == RED 
    
    #check if the spot has not already been processed or checked during the algorithm runtime.
    def is_open(self): 
        return self.color == GREEN 
    
    def is_barrier(self): 
        return self.color == BLACK 
    
    def is_start(self): 
        return self.color == ORANGE
    
    def is_end(self): 
        return self.color == PURPLE

    #ENFORCING METHODS // SETTERS
    #reset the color of the spot to assign it a specific role: 
    def reset(self): 
        self.color = WHITE
    
    def visit(self): 
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

    #METHOD TO DRAW THE SPOTS
    def draw_spot(self, window):  
        #drawing the rectangle spot -- rectangle argument is represented as a tuple of coordinates, size, and height. 
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.width))

    #METHOD TO UPDATE NEIGHBORS OF A SPOT. ONLY CALLED ONCE DURING THE INTIALIZATION OF THE PATH FINDING ALGORITHM.
    def update_neighbours(self, grid): 
        self.neighbours.clear()

        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier(): 
            self.neighbours.append(grid[self.row - 1][self.col])
        
        if self.row < (self.rows - 1) and not grid[self.row+1][self.col].is_barrier(): 
            self.neighbours.append(grid[self.row+1][self.col])
        
        if self.col > 0 and not grid[self.row][self.col-1].is_barrier(): 
            self.neighbours.append(grid[self.row][self.col-1])
        
        if self.col < (self.rows - 1) and not grid[self.row][self.col+1].is_barrier(): 
            self.neighbours.append(grid[self.row][self.col+1])   