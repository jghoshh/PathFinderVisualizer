from queue import PriorityQueue
import pygame

#HEURISTIC FUNCTION FOR A* ALGO (USING MANHATTAN DISTANCE). 
#Takes input of two point coordinates (tuples) and returns an int.
def h(p1, p2): 
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

#ACTUAL A* ALGO
def a_star(draw, grid, start, end): 
    count = 0
    open_set_queue = PriorityQueue()
    open_set_queue.put((0, count, start)) #(f-score, #insertion number (tie-breaker), actual node itself)
    came_from = {} #the parent of each node 
    g_score = {spot: float("inf") for row in grid.grid for spot in row} 
    g_score[start] = 0
    f_score = {spot: float("inf") for row in grid.grid for spot in row}
    f_score[start] = h(start.get_pos(), end.get_pos())

    open_set = {start} #to check whether a node is in the queue or not

    while not open_set_queue.empty(): 
        
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit()
        
        selected = open_set_queue.get()
        node = selected[2]
        open_set.remove(node)

        if node == end: 
            return True
            break

        for neighbour in node.neighbours: 
            h_score_neighbour = h(neighbour.get_pos(), end.get_pos()) #running the heuristic function on the current selected node. 
            g_score_neighbour = g_score[node] + 1 #adding the g-score, i.e. the distance from the start node to the current node, to 1 (the distance from any node to its direct neighbour). 
            
            if g_score_neighbour < g_score[neighbour]: 
                g_score[neighbour] = g_score_neighbour
                f_score[neighbour] = g_score_neighbour + h_score_neighbour
                came_from[neighbour] = node

            open_set.put(())
            open_set.add(neighbour)

        

            
        


