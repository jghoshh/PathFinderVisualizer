#DIJKSTRA ALGO
import heapq

#trace back from end spot and make the path.
def make_path(parent, end, draw):
    curr = end
    while (parent[curr] != None): 
        curr.make_path()
        draw()
        curr = parent[curr]
    end.make_end()

#ACTUAL A* ALGO
def dk(draw, grid, start, end): 
    distance = {spot: float('inf') for row in grid for spot in row}
    parent = {}
    visited = set()
    distance[start] = 0
    parent[start] = None
    insertion_count = 0
    q = [(distance[start], insertion_count, start)]
    
    while len(q) > 0: 
        
        curr_distance, curr_count, curr_spot = heapq.heappop(q)
        
        if (curr_spot == end): 
            make_path(parent, end, draw)
            break

        visited.add(curr_spot)
        
        for n in curr_spot.neighbours: 
            if n not in visited:
                r = curr_distance + 1
                if (r < distance[n]): 
                    insertion_count += 1
                    distance[n] = r
                    n.make_open()
                    parent[n] = curr_spot
                    heapq.heappush(q, (distance[n], insertion_count, n))
             
        if (curr_spot != start): 
            curr_spot.visit()
        
        draw()






