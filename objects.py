from p5 import *
from random import *
# from numpy import *
class circlies():
    # min_radius = 0.1
    # max_radius = 2
    def __init__(self, tempx, tempy, tempr):
        self.x = tempx
        self.y = tempy
        self.r = tempr
        
    def display(self):
        # no_stroke()
        ellipse_mode(mode='CENTER')
        # fill(255)
        z = randrange(255)
        v = randrange(255)
        u = randrange(255)
        fill(z, v, u)
        circle(self.x, self.y, self.r)
        