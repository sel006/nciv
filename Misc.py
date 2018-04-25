def check_limity(x, y,  ylim, xlim, prevx, YLIM):

    YLIM = ylim + 1 

    if y == ylim and x > xlim and prevx > xlim:
        return (-1)
    if y == YLIM:
        return (-1)
    if y < 0:
        return 1
    return 0

def check_limitx(x, y, ylim, xlim, prevy, XLIM):
    if x > xlim and y == ylim and prevy == ylim:
        return (-1)
    if x == XLIM:
        return (-1)
    if x < 0:
        return 1
    return 0
    
        
def inputx(char):
    if char == ord('l'):
        return 1
    elif char == ord('h'):
        return (-1)
    else:
        return 0

def inputy(char):
    if char == ord('j'):
        return 1
    elif char == ord('k'):
        return (-1)
    else:
        return 0
