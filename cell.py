n = 30 # height
m = 30 # width
scl = 20
border = 50
delay = 0.01
algo = None
moves = ((0, -1), (0, 1),
         (-1, 0), (1, 0))

class Cell(object):
    
    def __init__(self, walls=[1, 1, 1, 1]):
        
        # 0 - left
        # 1 - right
        # 2 - top
        # 3 - bottom
        
        self.walls = walls[:]
        self.visited = False
        self.depth = None
        
    def show(self, x, y):
        if self.walls[0]:
            line(x, y, x, y+scl)
        if self.walls[1]:
            line(x+scl, y, x+scl, y+scl)
        if self.walls[2]:
            line(x, y, x+scl, y)
        if self.walls[3]:
            line(x, y+scl, x+scl, y+scl)