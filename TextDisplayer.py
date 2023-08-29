import math


testTable = [
    [0, 1, 0, 0, 0, 1],
    [0, 1, 0, 1, 1, 1]
]

placeHolderList = []
placeHolderList2 = []
count = 0
randomValue = 0

def generateString(table):
    placeHolderList = ""
    for i, x in table:
        if i == 0:
            i = "||"
        else:
            i = "  "
        print(i)
        placeHolderList = placeHolderList + i
    return placeHolderList
def render(table):
    for i, x in table:
        randomValue = generateString(i)
        placeHolderList2.append(randomValue)  
        print(x)
        
        
generateString(testTable[0])
