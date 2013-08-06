'''
This is a program used to see how different values filled into the
parameters of "findLines" affected the lines drawn onto the image
'''

import SimpleCV
from SimpleCV import Camera
import time

images = [None,None]
images[0] = SimpleCV.Image('Image File Here')



img=images[0].scale(.2)

img = img.smooth()
img = img.dilate()
img = img.erode()

lines=img.findLines(threshold=2,maxlinegap=9,cannyth1=50,cannyth2=75) #edit these parameters
lines=lines.filter(abs(lines.angle())<100.0)
lines=lines.filter(80.0>abs(lines.angle()))
for line in lines:
    line.draw(color=SimpleCV.Color.GREEN,width=2)

img.show()


