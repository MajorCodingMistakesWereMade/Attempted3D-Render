import math
import time

import itertools
import threading
import sys


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
#here is the animation
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!     ')

t = threading.Thread(target=animate)
t.start()

placeHolderList = []
placeHolderList2 = []
count = 0
loadingBarCount = 0
randomValue = 0

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
        wait(0.0005)
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
        wait(0.005)
        loadingBarCount = loadingBar(loadingBarCount)
    print("DisplayingImage..")
    #for i, x in enumerate(placeHolderList2):
        #print(x)
        
        
render(testTable3)

done = True