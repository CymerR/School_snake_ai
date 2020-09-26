from pygame import *

class Snake(object):
    """docstring for Snake."""

    def __init__(self, position, ctrl_strategy=None,TILE_SIZE=16):
        self.x, self.y = position
        self.body = [(self.x,self.y)]
        self.length = 3
        self.TILE_SIZE = TILE_SIZE
        self.dx = 1
        self.dy = 0
        self.ctrl_strategy = ctrl_strategy
        self.init_body()

    """private """
    def init_body(self):
        for it in range(1,self.length):
            self.body.append((self.x + it, self.y))

    def move(self):
        self.x += self.dx
        self.y += self.dy
        self.body.append((self.x, self.y))
        self.body = self.body[-self.length:]

    def draw_self(self,sc, TILE_SIZE):
        [(draw.rect(sc,Color("green"),(i*TILE_SIZE,j*TILE_SIZE, TILE_SIZE, TILE_SIZE))) for i,j in self.body]


    def eat_apple(self):
        self.length += 1


    def get_head(self):
        return self.body[-1]


    def process_keys(self, keys=None, cells=None):
        if self.ctrl_strategy != None:
            self.dx, self.dy = self.ctrl_strategy.decide(keys, cells, prev_pos=(self.dx, self.dy))
