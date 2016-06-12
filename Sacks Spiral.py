import numpy as np
import matplotlib.pyplot as plt
import itertools
from math import *
from PIL import Image, ImageDraw
from Tkinter import *
import time

imagesize = 1500
hoogte = 1080
breedte = 1920

scalefactor = 2
squaresize = 3

fig = plt.figure(figsize=(18, 16))
plt.xlim(-500,500)
plt.ylim(-500,500)
ax = fig.add_subplot(111)

def isprime(getal):
    for i in range(2,int(sqrt(getal)) + 1):
        if getal % i == 0:
            return False
            break
    return True



number_frames = 0
list_primes = []

for i in range(0,100000):
    
    theta = sqrt(i) * 2 * pi
    r = sqrt(i)
    x = -cos(sqrt(i)*2*pi)*sqrt(i)
    y = sin(sqrt(i)*2*pi)*sqrt(i) 
    x = int(x *scalefactor)# + (breedte / 2)
    y = int(y *scalefactor)# + (hoogte / 2)
    
    if isprime(i):
        list_primes.append(i)
        ax.plot(x,y, linestyle = '', marker='o',color='r',markersize=3)
    
    if i % 50 == 0:
        plt.savefig('images/' + str(number_frames) +'.png', bbox_inches='tight')
        number_frames += 1
        
 

    
    


plt.show() #Show the last plot to confirm the iterations are complete
print len(list_primes)

      

