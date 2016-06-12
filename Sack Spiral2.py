# Part of the code has been borrowed from John Williamson
# http://www.dcs.gla.ac.uk/~jhw/spirals/

from math import *
from PIL import Image, ImageDraw
from Tkinter import *
import time



def isprime(getal): #determine whether a certain number is prime
    for i in range(2,int(sqrt(getal)) + 1): 
        if getal % i == 0:
            return False
            break
    return True

imagesize = 1500
hoogte = 1080
breedte = 1920

scalefactor = 2
squaresize = 3

master = Tk()

w = Canvas(master, width=breedte,height=hoogte,background='black',relief='raised')
w.pack()



for i in range(0,40000):
    theta = sqrt(i) * 2 * pi
    r = sqrt(i)
    x = -cos(sqrt(i)*2*pi)*sqrt(i)
    y = sin(sqrt(i)*2*pi)*sqrt(i) 
    x = int(x *scalefactor) + (breedte / 2)
    y = int(y *scalefactor) + (hoogte / 2)
    
    if isprime(i):
        #print i,":",x,y
        w.create_rectangle(x,y, x+squaresize, y+squaresize, fill="red")
    

mainloop()
      