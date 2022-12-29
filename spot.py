import pygame
from colors import *

#A CLASS FOR THE FUNDAMENTAL BUILDING BLOCK OF THE VISUALIZER.
class Spot: 
    def __init__(self, row, col, gap, total_rows): 
        self.row = row #which row this spot is located in. 
        self.col = col #which column this spot is located in. 
        self.gap = gap #how wide this spot is (all spots will have the same size). 
        self.x = col*gap #x-coordinate of the spot -- the location of the spot in terms of pygame. 
        self.y = row*gap #y-coordinate of the spot -- the location of the spot in terms of pygame.
        self.color = WHITE #base color of the spot. 
        self.neighbours = [] #neighbors of the spot -- to be utilized in the path finding algorithm. 
        self.rows = total_rows #if at anytime we need the total # of rows/columns in the grid, we call this. 
        #the reason why we have only one instance variable of rows is because the num. of rows and columns 
        #will be the same. 
    
    #BOOLEAN CHECKS OF STATE // GETTERS
    #returns the position of the spot in the matrix of spots defining the path finding maze. 
    #note. we are indexing by row, col, because we will be storing these spots in a matrix.  
    def get_pos(self):
        return self.row, self.col #returning position in matrix indexing format. 
    
    #check if the spot has already been processed and checked during the algorithm runtime.
    def checked(self): 
        return self.color == RED 
    
    #check if the spot has not already been processed or checked during the algorithm runtime.
    def not_checked(self): 
        return self.color == GREEN 
    
    #check if the spot is a barrier. 
    def is_barrier(self): 
        return self.color == BLACK 
    
    #check if the spot is the start node.  
    def is_start(self): 
        return self.color == ORANGE
    
    #check if the spot is the end node.
    def is_end(self): 
        return self.color == PURPLE
    
    #ENFORCING METHODS // SETTERS
    #reset the color of the spot to assign it a specific role: 
    def reset(self): 
        self.color = WHITE
    
    def check(self): 
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
        #drawing the rectangle spot -- rectangle argument is represented as a tuple of coordinates, size, and height. 
        pygame.draw.rect(window, self.color, (self.x, self.y, self.gap, self.gap))
    
    #checking and updating the neighbors of the given spot (checking left, down, right, and up).
    #we will only include a spot in the list of neighbors of another spot if it is not a barrier. 
    def update_neighbours(self, grid): 
        self.neighbours = []
        
        if self.row > 0 and not grid.grid[self.row-1][self.col].is_barrier(): 
            self.neighbours.append(grid.grid[self.row-1][self.col])
        
        if self.row < (self.total_rows - 1) and not grid.grid[self.row+1][self.col].is_barrier(): 
            self.neighbours.append(grid.grid[self.row+1][self.col])
        
        if self.col > 0 and not grid.grid[self.row][self.col-1].is_barrier(): 
            self.neighbours.append(grid.grid[self.row][self.col-1])
        
        if self.col < (self.total_rows - 1) and not grid.grid[self.row][self.col+1].is_barrier(): 
            self.neighbours.append(grid.grid[self.row][self.col+1])   

    #LESS THAN FUNCTION
    #define a way to calculate if a spot is less than another spot. Always return false here, because ...
    def __lt__(self, other): 
        return False