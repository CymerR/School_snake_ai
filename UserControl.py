from pygame import *


class UserControl(object):
    """docstring for UserControl."""

    def __init__(self):
        print("User controller init!")


    def decide(self, keys,cells=None, prev_pos=(0,0)):
        dx,dy = prev_pos
        if keys[K_w] and dy !=  1:
            dx, dy = 0,-1
        if keys[K_s] and dy != -1:
            dx, dy = 0, 1
        if keys[K_a] and dx !=  1:
            dx, dy =-1, 0
        if keys[K_d] and dx != -1:
            dx, dy = 1, 0
        return (dx,dy)
