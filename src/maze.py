from time import sleep
from algorithms import *
from cell import *

class Maze(object):
    
    def __init__(self):
        self.it = [[Cell() for j in range(m)] for i in range(n)]
        self.path = []
        self.ready = False
        self.maxDepth = 0
        
    def __getitem__(self, index):
        return self.it[index]
    
    def show(self):
        stroke(255)
        x = y = border
        for i in range(n):
            for j in range(m):
                self[i][j].show(x, y)
                x += scl
            y += scl
            x = border
            
    def showPath(self):
        stroke(255, 0, 255)
        strokeWeight(scl/4)
        noFill()
        beginShape()
        for i, j in self.path:
            x = border + j*scl + scl/2
            y = border + i*scl + scl/2
            vertex(x, y)
        endShape()
        strokeWeight(1)
    
    def neighbors(self, cell):
        neigh = []
        i, j = cell
        conds = (j > 0, j+1 < m, i > 0, i+1 < n)
        for k in range(4):
            iinc, jinc = moves[k]
            if conds[k] and not self[i+iinc][j+jinc].visited:
                neigh.append((i+iinc, j+jinc))
        return neigh
    
    def adjacent(self, cell):
        adj = []
        i, j = cell
        walls = self[i][j].walls
        for k in range(4):
            iinc, jinc = moves[k]
            if not walls[k] and self[i+iinc][j+jinc].visited:
                adj.append((i+iinc, j+jinc))
        return adj
    
    def destroyWall(self, cell1, cell2):
        i1, j1 = cell1
        i2, j2 = cell2
        if i1 == i2:
            w = int(j1 < j2)
            self[i1][j1].walls[w] = 0
            self[i2][j2].walls[1-w] = 0
        else:
            w = int(i1 < i2)
            self[i1][j1].walls[2+w] = 0
            self[i2][j2].walls[3-w] = 0
        sleep(delay)    
    
    def findPath(self):
        for i in range(n):
            for j in range(m):
                self[i][j].visited = True
        first = (0, 0)
        stack = [first]
        while stack:
            i, j = current = stack[-1]
            self[i][j].visited = False
            self[i][j].depth = len(stack)
            self.maxDepth = max(self.maxDepth, self[i][j].depth)
            neighbors = self.adjacent(current)
            if neighbors:
                stack.append(neighbors[0])
            else:
                stack.pop()
            if not self.path and stack[-1] == (n-1, m-1):
                self.path = stack[:]
        
    def floodFill(self):
        noStroke()
        for i in range(n):
            for j in range(m):
                alfa = 255.0*self[i][j].depth/self.maxDepth
                fill(0, 255, 0, alfa)
                x = border + j*scl
                y = border + i*scl
                rect(x+1, y+1, scl-1, scl-1)
                    
    dfs = dfs
    kruskal = kruskal
    prim = prim
    wilson = wilson
    division = division
        