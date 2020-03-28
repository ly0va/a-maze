# vim: ft=python
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
toggles = {'f': False, 'c': False, 'p': False}

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
        if toggles['f']:
            maze.floodFill()
        if toggles['c']:
            maze.showPath()
        if toggles['p']:
            you.showPath()
            me.showPath()
        showGame()

def keyPressed():
    if not maze.ready: 
        return
    if key == 'R': 
        restart()
    if key in toggles: 
        toggles[key] = not toggles[key]
    if not Player.gameOver:
        you.move(keyCode)
        me.move(keyCode)
    
def showGame():
    you.showDest()
    me.showDest()
    you.show()
    me.show()
    you.winner()
    me.winner()
    Player.overlap(you, me)
    
def generate():
    a = algo
    if a is None:
        while str(key) not in "12345": sleep(1)
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
