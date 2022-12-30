import os
import pygame
import algos.bfs
import algos.dk
import algos.dfs
from constants.colors import *
from models.spot import *
from models.grid import *
from helpers import *
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

#MAIN PROGRAM
#setting up the pygame window size and creating a 'window' object. 
size = 800
WINDOW = pygame.display.set_mode((size, size))
GRAPH_DICT = {"A": algos.dk.dk, "B": algos.bfs.bfs, "D": algos.dfs.dfs, "DI": algos.dk.dk}
pygame.display.set_caption("Path Finding Visualizer")


#main program to run our visualizer.
def main(surface, rows, size): 
    
    #create the grid.
    grid = Grid(rows, size)

    #create some variables to account for the starting and ending Spots.
    start = None
    end = None

    #variable to indicate whether our algo has started or not. Used to prevent users from interfering
    #with the execution of the algo during runtime.
    started = False

    #flag variable to keep our main program running, displaying our UI, and looking out for events.
    run = True
    prompt = None
    i = 0

    #the purpose of this while loop is to run the main program until the user quits the program.
    #inside the loop, we first draw the grid and then listen for any events on the grid. 
    #if there is an event, the program registers the event and takes appropriate action.
    while run: 

        if (prompt and i == 0): 
            print(prompt)
            i += 1

        #draw the grid intially.
        grid.draw_grid(surface)

        #if the algorithm has started, then loop back. Do not proceed to the next statements and register events.
        if started == True: 
            continue
        
        #get all events that have occured, iterate over them, and examine them one by one.
        for event in pygame.event.get():
            #if the event that occured involved user pressing the X button, then quit the program.
            if event.type == pygame.QUIT: 
                run = False

            #if user didn't quit the program, then check for mouse clicks. 
            #if user pressed the left mouse button, then it is assumed that the user wants to place a spot.
            #in the following statements, it is checked whether the user wants to place a starting spot,
            #an ending spot, or a barrier spot.
            if pygame.mouse.get_pressed()[0]:
                
                #get the original position of the starting spot with respect to pygame coordinates.
                pos = pygame.mouse.get_pos()

                #get the normalized position of the clicked spot with respect to the grid matrix. 
                col, row = get_clicked_pos(pos, rows, size)

                #find the actual spot in the grid matrix using the normalized indices retrieved above.
                spot = grid.grid[row][col]

                #if a starting spot hasn't been initialized, then assume that user is creating a starting spot.
                #place a starting spot by calling make_start() method of spot.
                if start == None and spot != end: 
                    start = spot 
                    start.make_start()

                #if a starting spot has been initialized, but not an ending spot,
                #then place an ending spot by calling make_end() method of spot.
                elif end == None and spot != start: 
                    end = spot
                    end.make_end()

                #in the case that a starting spot and an ending spot have been placed, 
                #then the selected spot is a barrier. 
                #need to check that selected spot is not the starting spot or the ending
                #spot to prevent un-wanted overwriting.
                elif spot != end and spot != start: 
                    spot.make_barrier()

            #if user pressed the right mouse button, then it is assumed that the user wants to erase a spot.
            elif pygame.mouse.get_pressed()[2]: 

                #get the original position of the starting spot.
                pos = pygame.mouse.get_pos()

                #get the normalized position of the clicked spot.
                col, row = get_clicked_pos(pos, rows, size)

                #find the actual spot in the grid matrix using the normalized indices retrieved above.
                spot = grid.grid[row][col]

                #if the spot that is about to be reset is the starting spot, then make the
                #start variable containing the starting spot contain None, as there is no starting
                #spot anymore. 
                if spot == start: 
                    start = None

                #if the spot that is about to be reset is the ending spot, then make the
                #end variable containing the ending spot contain None, as there is no ending
                #spot anymore. 
                elif spot == end: 
                    end = None

                #reset the spot to be the base colour of white.
                spot.reset()
            
            #if user pressed the space key, then run the algorithm. 
            #However, this only works if the algorithm has not already started and if there are starting and ending spots.
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_SPACE and started == False and start and end:
                    
                    for row in grid.grid: 
                        for spot in row: 
                            if spot != start and spot != end and not spot.is_barrier(): 
                                spot.reset()

                    #Here, we'll have checks for which algorithm the user wants to run: DFS, BFS, A*, or DIJKSTRA
                    #GET INPUT FROM USERS FIRST

                    print()
                    inp = ask_input()
                    print()
                    graph_dict = {"A": algos.dk.dk, "B": algos.bfs.bfs, "D": algos.dfs.dfs, "DI": algos.dk.dk}
                    
                    while True:
                        started = True
                        if inp in graph_dict:
                            for row in grid.grid: 
                                for spot in row: 
                                    spot.update_neighbours(grid.grid)
                                    if spot != start and spot != end and not spot.is_barrier(): 
                                            spot.reset()
                            graph_dict[inp](lambda: grid.draw_grid(surface), grid.grid, start, end)
                        else: 
                            if (inp != "R" and inp != "Q"): 
                                break
                                started = False
                            elif inp == "Q": 
                                run = False
                                break
                            else:
                                for row in grid.grid: 
                                    for spot in row: 
                                        if spot != start and spot != end and not spot.is_barrier(): 
                                            spot.reset()
                                grid.draw_grid(surface)
                                started = False
                                prompt = "Visualizer has been reset. Please press the space key to start the visualizer again."
                                i = 0
                                break
                        inp = ask_input()
                        print()
    pygame.quit()

def ask_input(): 
    return str(input("Enter the code for the path-finding algorithm that you want to visualize\n(B for BFS, D for DFS, A for A*, DI for Dijkstra, R to reset grid, or Q to quit): ")).strip().upper()

if __name__ == "__main__": 
    ROWS = 50
    main(WINDOW, ROWS, size) 
