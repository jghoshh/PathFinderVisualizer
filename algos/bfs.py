#BFS ALGO
queue = []

def make_path(parent, end, draw):
    curr = end
    while (parent[curr] != None): 
        curr.make_path()
        draw()
        curr = parent[curr]
    end.make_end()

#ACTUAL BFS ALGO
def bfs(draw, grid, start, end): 
    visited = set()
    parent = {}
    queue.append(start)
    parent[start] = None
    
    while queue: 
        curr = queue.pop(0)
        
        if (curr == end):
            make_path(parent, end, draw)
            return True

        visited.add(curr)

        for n in curr.neighbours: 
            if n not in visited:
                visited.add(n) 
                queue.append(n)
                n.make_open()
                parent[n] = curr
    
        if (curr != start): 
            curr.visit()

        draw()
    return False

