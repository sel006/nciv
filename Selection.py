def tall(pictotal, page8_count, last_page8_size, page):
    offset = 2
    wmax = 1
    hmax = 3
    WMAX = 1
    HMAX = 3
    maxnum = 0
    pic = []
    if len(pictotal) <= 8:
        pic = pictotal
    else:
        if page == page8_count:
           for x in range(0, last_page8_size):
                pic.append(pictotal[x+(page*8)])
        else:
           for x in range(0, 8):
                pic.append(pictotal[x+(page*8)])

    maxnum = len(pic)
    tmaxnum = maxnum - 1
    flag = 0
    for x in range(0, HMAX+1):
        if not flag:
            if tmaxnum <= (x*offset)+WMAX:
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

    vals = []
    vals.append(wmax)
    vals.append(hmax)
    vals.append(WMAX+1)
    vals.append(HMAX+1)
    vals.append(maxnum)
    vals.append(pic)
    return vals

import sys

def wide(pictotal, page12_count, last_page12_size, page):
    wmax = 3
    hmax = 2
    WMAX = 3
    HMAX = 2
    offset = 4
    pic = []
    if len(pictotal) <= 12:
        pic = pictotal
    else:
        if page == page12_count:
            for x in range(0, last_page12_size):
                pic.append(pictotal[x+(page*12)])
        else:
            for x in range(0,12):
                pic.append(pictotal[x+(page*12)])

    maxnum = len(pic)
    tmaxnum = maxnum - 1
    flag = 0
    for x in range(0, HMAX+1):
        if not flag:
            if tmaxnum <= (x*offset)+WMAX:
                hmax = x
                flag = 1
    flag = 0
    for x in range(0, HMAX+1):
        if not flag:
            if tmaxnum <= (x*offset)+WMAX:
                wmax = tmaxnum-(x*offset)
                flag = 1

    if maxnum < 4:
        HMAX = 0
        WMAX = tmaxnum 

    vals = []
    vals.append(wmax)
    vals.append(hmax)
    vals.append(WMAX+1)
    vals.append(HMAX+1)
    vals.append(maxnum)
    vals.append(pic)
    return vals
