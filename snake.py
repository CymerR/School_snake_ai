from pygame import *

class Snake(object):
    """docstring for Snake."""

    def __init__(self, posx,posy, TILE_SIZE=16):
        self.x = posx
        self.y = posy
        self.body = [(self.x,self.y)]
        self.length = 3
        self.TILE_SIZE = TILE_SIZE
        self.dx = 1
        self.dy = 0
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


    def process_keys(self, keys):
        if keys[K_w]:
            self.dx, self.dy =  0, -1
        if keys[K_s]:
            self.dx, self.dy =  0,  1
        if keys[K_a]:
            self.dx, self.dy = -1,  0
        if keys[K_d]:
            self.dx, self.dy =  1,  0
