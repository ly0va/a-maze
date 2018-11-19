from threading import Thread
from time import sleep
from player import Player
from maze import Maze
from cell import *

maze = Maze()
you = Player(1, maze)
me = Player(2, maze)
x = m*scl + 2*border
y = n*scl + 2*border

def setup():
    size(x, y)
    textSize(border/2)
    textAlign(CENTER, CENTER)
    strokeJoin(ROUND)
    Thread(target=generate).start()

def draw():
    if not maze.ready:
        background(51)
        maze.show()
    else:
        background(bg)
        if key == 'p':
            maze.showPath()
        if key == 'f':
            maze.floodFill()
        showGame()

def keyPressed():
    
    if not maze.ready: return
    if key == 'R': restart()
    if not Player.gameOver:
        you.move(keyCode)
        me.move(keyCode)
    
def showGame():
    you.showDest()
    me.showDest()
    # if not set(you.path) & set(me.path):
    #     you.showPath()
    #     me.showPath()
    you.show()
    me.show()
    you.winner()
    me.winner()
    Player.overlap(you, me)
    
def generate():
    a = algo
    if a is None:
        while key not in {'1', '2', '3', '4', '5'}: sleep(1)
        algos = ['dfs', 'kruskal', 'prim', 'wilson', 'division']
        a = algos[int(key)-1]
    getattr(maze, a)()
    maze.findPath()
    getBackground()
    maze.ready = True
    
def getBackground():
    global bg
    noLoop()
    redraw()
    sleep(0.2)
    bg = copy()
    loop()
    
def restart():
    global maze, you, me
    maze = Maze()
    you = Player(1, maze)
    me = Player(2, maze)
    Player.gameOver = False
    Thread(target=generate).start()