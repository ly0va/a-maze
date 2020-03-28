from random import randint, choice
from cell import n, m

class DSU:
    
    def __init__(self):
        self.parent = {}
        
    def findRoot(self, v):
        parent = self.parent
        if v not in parent:
            return v
        else:
            parent[v] = self.findRoot(parent[v])
            return parent[v]
        
    def unite(self, u, v):
        u = self.findRoot(u)
        v = self.findRoot(v)
        if u != v:
            self.parent[u] = v
        
    def together(self, u, v):
        return self.findRoot(u) == self.findRoot(v)

            
def dfs(self):
    first = (randint(0, n-1), randint(0, m-1))
    stack = [first]
    while stack:
        i, j = current = stack[-1]
        self[i][j].visited = True
        neighbors = self.neighbors(current)
        if neighbors:
            neigh = choice(neighbors)
            stack.append(neigh)
            self.destroyWall(current, neigh)
        else:
            stack.pop()
            
def prim(self):
    i, j = first = randint(0, n-1), randint(0, m-1)
    self[i][j].visited = True
    tree = [first]
    while tree:
        u = choice(tree)
        neighbors = self.neighbors(u)
        if neighbors:
            i, j = v = choice(neighbors)
            self.destroyWall(u, v)
            self[i][j].visited = True
            tree.append(v)
        else:
            tree.remove(u)
    
def kruskal(self):
    dsu = DSU()
    edges = 0
    while edges != n*m-1:
        u = randint(0, n-1), randint(0, m-1)
        v = choice(self.neighbors(u))
        if not dsu.together(u, v):
            dsu.unite(u, v)
            self.destroyWall(u, v)
            edges += 1
            
def wilson(self):
    first = randint(0, n-1), randint(0, m-1)
    tree = {first}
    while len(tree) != n*m:
        u = randint(0, n-1), randint(0, m-1)
        if u in tree: continue
        stack = [u]
        while stack[-1] not in tree:
            current = stack[-1]
            neighbors = self.neighbors(current)
            neigh = choice(neighbors)
            if neigh in stack:
                index = stack.index(neigh)
                stack = stack[:index+1]
            else:
                stack.append(neigh)
        for i in range(len(stack)-1):
            u = stack[i]
            v = stack[i+1]
            self.destroyWall(u, v)
        tree.update(stack)      
    
def division(self):
    def _divide(y, x, h, w):
        if w == h == 1: return
        a = int(h < w) if h != w else randint(0, 1)
        j = randint(a, w-1)
        i = randint(1-a, h-1)
        u = (y+i-1+a, x+j-a)
        v = (y+i, x+j)
        self.destroyWall(u, v)
        if a:
            _divide(y, x, h, j)
            _divide(y, x+j, h, w-j)
        else:
            _divide(y, x, i, w)
            _divide(y+i, x, h-i, w)
    _divide(0, 0, n, m)