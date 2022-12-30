#A STAR ALGO
import pygame

#HEURISTIC FUNCTION FOR A* ALGO (USING MANHATTAN DISTANCE). 
#Takes input of two point coordinates (tuples) and returns an int.
def h(p1, p2): 
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

def make_path(parent, end, draw):
    curr = end
    while (parent[curr] != None): 
        curr.make_path()
        draw()
        curr = parent[curr]
    end.make_end()

#ACTUAL A* ALGO
def a_star(draw, grid, start, end): 
    pass
