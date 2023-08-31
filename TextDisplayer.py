import math
import time

import itertools
import threading
import sys

# https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm

def wait(a):
    time.sleep(a)
    

testTable = [
    [1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 1],
    
]

testTable2 = [
    [1, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 1],
    [1, 1, 1, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 1],
]

testTable3 = [
    [0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0],
    [1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1],
    [0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1],

]


done = False
#NOT MY CODE
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\Rendered!     ')

t = threading.Thread(target=animate)
t.start()

# https://github.com/encukou/bresenham/blob/master/bresenham.py

def bresenham(x0, y0, x1, y1):
    """Yield integer coordinates on the line from (x0, y0) to (x1, y1).

    Input coordinates should be integers.

    The result will contain both the start and the end point.
    """
    dx = x1 - x0
    dy = y1 - y0

    xsign = 1 if dx > 0 else -1
    ysign = 1 if dy > 0 else -1

    dx = abs(dx)
    dy = abs(dy)

    if dx > dy:
        xx, xy, yx, yy = xsign, 0, 0, ysign
    else:
        dx, dy = dy, dx
        xx, xy, yx, yy = 0, ysign, xsign, 0

    D = 2*dy - dx
    y = 0

    for x in range(dx + 1):
        yield x0 + x*xx + y*yx, y0 + x*xy + y*yy
        if D >= 0:
            y += 1
            D -= 2*dx
        D += 2*dy


#ok back to stuff that is my code
placeHolderList = []
placeHolderList2 = []
count = 0
loadingBarCount = 0
randomValue = 0
acessTableThing = 0

def accessTableLocation(inputTable, xCord, yCord):
    acessTableThing = inputTable[xCord]
    acessTableThing = acessTableThing[yCord]
    return acessTableThing

def writeTableLocation(inputTable, xCord, yCord, writeTable):
    acessTableThing = inputTable[xCord]
    acessTableThing[yCord] = writeTable
 

def loadingBar(loadingBarCount):
    #print(f'Step {loadingBarCount}')
    loadingBarCount += 1
    return loadingBarCount


def generateString(inputTable):
    loadingBarCount = 0
    count = 0
    placeHolderList = ""
    for i in inputTable:
        count += 1
        #print(i)
        if i == 1:
            i = "||"
        else:
            i = "--"
        #print(i)    
        loadingBarCount = loadingBar(loadingBarCount)

        placeHolderList = placeHolderList + i
    #print(placeHolderList)
    ## placeHolderList = placeHolderList[2:]
    return placeHolderList
def render(inputTable):
    loadingBarCount = 0
    print("ClearingTable..")
    placeHolderList2.clear()
    print("AssigningValues..")
    for i in inputTable:
        randomValue = generateString(i)
        placeHolderList2.append(randomValue)
        loadingBarCount = loadingBar(loadingBarCount)
        wait(0.05)
    print("DisplayingImage..")
    for i, x in enumerate(placeHolderList2):
        print(x)
        
        
render(testTable3)

done = True