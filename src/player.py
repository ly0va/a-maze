from cell import *

class Player(object):
    
    gameOver = False
    
    def __init__(self, id, maze):
        self.maze = maze
        if id == 1:
            self.pos = [0, 0]
            self.keys = (65, 68, 87, 83)
            self.clr = color(255, 0, 0)
            self.label = "Red wins!"
            self.destination = [n-1, m-1]
        elif id == 2:
            self.pos = [n-1, m-1]
            self.keys = (37, 39, 38, 40)
            self.clr = color(0, 0, 255)
            self.label = "Blue wins!"
            self.destination = [0, 0]
        i, j = self.pos
        self.spos = (border + j*scl + scl/2, 
                     border + i*scl + scl/2)
        self.path = [tuple(self.pos)]
        self.pathFlag = True
        
    def show(self):
        fill(self.clr)
        stroke(255)
        smoothness = 0.2
        i, j = self.pos
        sx = border + j*scl + scl/2
        sy = border + i*scl + scl/2
        px, py = self.spos
        x = lerp(px, sx, smoothness)
        y = lerp(py, sy, smoothness)
        self.spos = (x, y)
        ellipse(x, y, scl/2, scl/2)
        
    def showDest(self):
        fill(self.clr)
        noStroke()
        i, j = self.destination
        x = border + j*scl
        y = border + i*scl
        rect(x+1, y+1, scl-1, scl-1)
    
    def showPath(self):
        stroke(self.clr, 200)
        strokeWeight(scl/4)
        noFill()
        beginShape()
        l = len(self.path) - self.pathFlag
        for i, j in self.path[:l]:
            x = border + j*scl + scl/2
            y = border + i*scl + scl/2
            vertex(x, y)
        vertex(*self.spos)
        endShape()
        strokeWeight(1)
        
    def move(self, dir):
        i, j = self.pos
        for k in range(4):
            if not self.maze[i][j].walls[k] and dir == self.keys[k]:
                self.pos[0] += moves[k][0]
                self.pos[1] += moves[k][1]
                pos = tuple(self.pos)
                self.pathFlag = pos not in self.path
                if not self.pathFlag:
                    self.path.pop()
                else:
                    self.path.append(pos)
         
    def winner(self):
        if self.pos == self.destination:
            fill(self.clr)
            text(self.label, width/2, border/2)
            Player.gameOver = True
        
    @staticmethod
    def overlap(one, two):
        eps = 1
        if abs(one.spos[0] - two.spos[0]) < eps and \
           abs(one.spos[1] - two.spos[1]) < eps:
            fill(255, 255, 255)
            x, y = one.spos
            ellipse(x, y, scl/2, scl/2)
