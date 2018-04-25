import os
import curses 
import subprocess
import sys
import Image
import Window
import Misc
import Selection

#Initializes ncurses related settings
def initwin():
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(1)
    return stdscr

#Terminates all ncurses related settings
def endall():
    curses.nocbreak()
    stdscr.keypad(0)
    curses.echo()
    curses.endwin()

cwd = os.getcwd()

#pictures = filter(lambda x: x.endswith('.jpg') or x.endswith('.png'), os.listdir('/home/dave/Pictures/testdir'))
pictures = filter(lambda x: x.endswith('.jpg') or x.endswith('.png'), os.listdir(cwd))
pictotal = []
for x in pictures:
    pictotal.append(x)

# Initializes curses and creates the window object
stdscr = initwin()
curses.start_color()
curses.use_default_colors()
curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_BLUE)

# Turns off cursor
curses.curs_set(0)

stdscr.refresh()

cursx = 0
cursy = 0

prevy = 0
prevx = 0

page = 0
prevpage = page

if 1:
    page8_count = int(len(pictotal)/8)
    last_page8_size = len(pictotal)-(page8_count*8)
    page12_count = int(len(pictotal)/12)
    last_page12_size = len(pictotal)-(page12_count*12)

height,width = stdscr.getmaxyx()

if (2*height)>width:
    dir = 'k'
else:
    dir = 'k'

resetflag = 0

while 1:

    stdscr.refresh()

    height,width = stdscr.getmaxyx()

    prev_dir = dir

    Sflag = 0

    if (2*height)>width:
        dir = 'l'
    else:
        dir = 'w'

    if dir != prev_dir or prevpage != page:
        if prevpage != page:
            stdscr.clear()
            stdscr.refresh()
        pic = []
        maxnum = 0
        if dir == 'l':
            offset = 2
            vals = Selection.tall(pictotal, page8_count, last_page8_size, page)
            wmax = vals[0]
            hmax = vals[1]
            WMAX = vals[2]
            HMAX = vals[3]
            maxnum = vals[4]
            pic = vals[5]
        else:
            offset = 4
            vals = Selection.wide(pictotal, page12_count, last_page12_size, page)
            wmax = vals[0]
            hmax = vals[1]
            WMAX = vals[2]
            HMAX = vals[3]
            maxnum = vals[4]
            pic = vals[5]
        Sflag = 1

    cursx += Misc.check_limitx(cursx, cursy, hmax, wmax, prevy, WMAX)
    cursy += Misc.check_limity(cursx, cursy, hmax, wmax, prevx)

    index = cursy * offset + cursx

    wins = Window.init_windows(height, width, index, maxnum)
    Window.draw_windows(wins)
    if Sflag or resetflag:
        ims = Image.init_images(pic, height, width)
        Image.draw_images(ims)
    resetflag = 0

    prevpage = page

    c = stdscr.getch()
    if c == ord('q'):
        endall()
        break

    if c == ord('f'):
        stdscr.clear()
        stdscr.refresh()
        Image.fullscreen(ims[index].name, height, width)
        while 1:
            d = stdscr.getch()
            if d == ord('f'):
                stdscr.clear()
                resetflag = 1
                break
    if c == ord('p') and page > 0:
        page -= 1

    if c == ord('r'):
        resetflag = 1

    if (2*height)>width:
        if c == ord('n') and page < page8_count:
            prevpage = page
            page += 1
    else:
        if c == ord('n') and page < page12_count:
            prevpage = page
            page += 1

    prevx = cursx
    prevy = cursy

    cursx += Misc.inputx(c)
    cursy += Misc.inputy(c)
        
    Window.draw_windows(wins)
