from random import *
from p5 import *
from cyberbrain import *
import objects as cr
# from numpy.random import default_rng
New_Circlly = None

def setup():

    global New_Circlly
    size(800, 600)
 
def draw():
    global New_Circlly
    # no_loop()
     #background(157, 255, 255) pretty blue
    background(25)
    a = random_gaussian(mean=400, std_dev=200)
    b = random_gaussian(mean=300, std_dev=150)
    c = random_gaussian(mean=100, std_dev=200)
    
    try:
        New_Circlly = cr.circlies(a,b,c)
    except:
        print("A is",a,"B is",b,"C is",c)
        print('error at defining values and making circle')
        exit()
        
    try:
        New_Circlly.display()
    except:
        print("A is",a,"B is",b,"C is",c)
        print('error at display of circle')
        exit()

run(frame_rate=2)
