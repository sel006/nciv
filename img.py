import os
import curses 
import subprocess
import sys
import Image
import Window
import Misc

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

pictures = filter(lambda x: x.endswith('.jpg') or x.endswith('.png'), os.listdir('/path/to/folder'))
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

if len(pictotal) > 8:
    page8_count = int(len(pictotal)/8)
    last_page8_size = len(pictotal)-(page8_count*8)

if len(pictotal) > 12:
    page12_count = int(len(pictotal)/12)
    last_page12_size = len(pictotal)-(page12_count*12)


while 1:

    stdscr.refresh()

    height,width = stdscr.getmaxyx()
    pic = []
    maxnum = 0

    if (2*height)>width:
        offset = 2
        wmax = 1
        hmax = 3
        WMAX = 1
        HMAX = 3
        if len(pictotal) <= 8:
            pic = pictotal
            maxnum = len(pic)
        else:
            if page == page8_count:
                for x in range(0, last_page8_size):
                    pic.append(pictotal[x+(page*8)])
                maxnum = len(pic)
            else:
                for x in range(0, 8):
                    pic.append(pictotal[x+(page*8)])
                maxnum = len(pic)
        if 1:
            tmaxnum = maxnum - 1
            flag = 0
            for x in range(0, hmax+1):
                if not flag:
                    if tmaxnum <= (x*offset)+wmax:
                        hmax = x
                        flag = 1
            flag = 0
            for x in range(0, HMAX+1):
                if not flag:
                    if tmaxnum <= (x*offset)+WMAX:
                        wmax = tmaxnum-(x*offset)
                        flag = 1
            if maxnum < 2:
                WMAX = wmax
        else:
            for x in range(page, page+8):
                pic.append(pictotal[x])
            maxnum = 8

    else:
        wmax = 3
        hmax = 2
        WMAX = 3
        HMAX = 2
        offset = 4
        if len(pictotal) <= 12:
            pic = pictotal
            maxnum = len(pic)
        else:
            if page == page12_count:
                for x in range(0, last_page12_size):
                    pic.append(pictotal[x+(page*12)])
                maxnum = len(pic)
            else:
                for x in range(0, 12):
                    pic.append(pictotal[x+(page*12)])
                maxnum = len(pic)
        if 1:
            tmaxnum = maxnum - 1
            flag = 0
            for x in range(0, hmax):
                if not flag:
                     if tmaxnum <= (x*offset)+wmax:
                         hmax = x
                         flag = 1
            flag = 0
            for x in range(0, HMAX):
                if not flag:
                    if tmaxnum <= (x*offset)+WMAX:
                        wmax = tmaxnum-(x*offset)
                        flag = 1
            if maxnum < 4:
                WMAX = wmax
        else:
            for x in range(page, page+12):
                pic.append(pictotal[x])
            maxnum = 8

    cursx += Misc.check_limitx(cursx, cursy, hmax, wmax, prevy, WMAX)
    cursy += Misc.check_limity(cursx, cursy, hmax, wmax, prevx)

    index = cursy * offset + cursx

    wins = Window.init_windows(height, width, index, maxnum)
    ims = Image.init_images(pic, height, width)

    Window.draw_windows(wins)
    Image.draw_images(ims)

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
                break
    if c == ord('p') and page > 0:
        page -= 1

    if (2*height)>width:
        if c == ord('n') and page < page8_count:
            page += 1
    else:
        if c == ord('n') and page < page12_count:
            page += 1

    prevx = cursx
    prevy = cursy

    cursx += Misc.inputx(c)
    cursy += Misc.inputy(c)
        
    Window.draw_windows(wins)
#    stdscr.clear()
