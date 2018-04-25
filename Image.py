import os
import curses
import subprocess
import sys

class Image(object):
            # This is the image which is drawn on the terminal
    # It must be its own class. Combining the Image and Thumbnail class
    # breaks the program

    def __init__(self, name, x, y, height, width):

        self.name = name
        self.x = image_x(x)
        self.y = image_y(y)
        self.width = image_width(width)
        self.height = image_height(height)

    def draw_img(self):

	# Formatting the arguments passed to w3mimgdisplay, and running
	# the command
        info = buildarg(self.name, self.x, self.y, self.height, self.width)
        subprocess.run(["/usr/libexec/w3m/w3mimgdisplay"], universal_newlines=True,
            input=info)

def init_images(pics, my, mx):

    images = []
    n = len(pics)

    if (2*my)>mx:
        yran = 4
        xran = 2
        hprop = int(.25*my)
        wprop = int(.42*mx)
    else:
        yran = 3
        xran = 4
        hprop = int(.30*my)
        wprop = int(.25*mx)

    for y in range(0,yran):
        imy = y * hprop 
        for x in range(0,xran):
            if n == 0:
                return images
            pic = pics[(y*xran)+x]
            imx = x * wprop 
            img = Image(pic, imx, imy, hprop, wprop)
            images.append(img)
            n -= 1
    return images

def draw_images(ims):
    for x in ims:
        x.draw_img()

#Builds the arguments piped into w3mimgdisplay
def buildarg(filename, x, y, height, width):
    return '0;1;'+str(x)+';'+str(y)+';'+str(width)+';'+str(height)+';;;;;'+ filename +'\n4;\n3;\n'

#Calculate the height and width of image based on window size
def image_y(y):
    return (18*y+10)
def image_x(x):
    return (9*x+7)
def image_height(h):
    return (18*h-27)
def image_width(w):
    return (9*w-19)

def fullscreen(pic, height, width):
    full = Image(pic, 0, 0, height, width)
    full.draw_img()
