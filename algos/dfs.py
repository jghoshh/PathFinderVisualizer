
stack = []

def make_path(parent, end, draw):
    curr = end
    while (parent[curr] != None): 
        curr.make_path()
        draw()
        curr = parent[curr]
    end.make_end()

def dfs(draw, grid, start, end): 
    visited = set()
    parent = {}
    stack.append(start)
    parent[start] = None
    
    while stack: 
        curr = stack.pop()
        
        if (curr == end):
            make_path(parent, end, draw)
            return True

        visited.add(curr)

        for n in curr.neighbours: 
            if n not in visited:
                stack.append(n)
                n.make_open()
                parent[n] = curr
    
        if (curr != start): 
            curr.visit()

        draw()
    return False