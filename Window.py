import os
import curses
import subprocess
import sys

class Window(object):
        
    # The window/box which appears around the image.
    def __init__(self, x, y, height, width):

        self.x = x
        self.y = y
        self.height = height 
        self.width = width

        self.window = curses.newwin(self.height, self.width,
        			    self.y, self.x)
    # Called every time the object changes
    def update(self):
        self.window.refresh()
    def draw_border(self):
        self.window.box()

    def coloron(self):
        self.window.attrset(curses.A_REVERSE)
    def coloroff(self):
        self.window.attrset(curses.A_NORMAL)

#Draw grid of windows
def init_windows(my, mx, index, num):
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

    windows = []
    for y in range(0,yran):
        winy = y * hprop
        for x in range(0, xran):
            if num == 0:
                windows[index].coloron()
                return windows
            winx = x * wprop 
            win = Window(winx, winy, hprop, wprop)
            windows.append(win)
            num -= 1

    windows[index].coloron()
    return windows

def draw_windows(wins):
    for x in wins:
        x.draw_border()
        x.update()
