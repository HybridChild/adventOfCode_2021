import os
import math


# --- Start here ---
scriptDir = os.path.dirname(__file__)
relFilePath = 'input.txt'
absFilePath = os.path.join(scriptDir, relFilePath)

with open(absFilePath) as inputFile:
    inputStr = inputFile.read()

inputStr = inputStr[13:]

xStr = inputStr[inputStr.find('x=')+2 : inputStr.find(',')]
xStr = xStr.split('..')
xCoords = {'low': int(xStr[0]), 'high': int(xStr[1])}
yStr = inputStr[inputStr.find('y=')+2 : ]
yStr = yStr.split('..')
yCoords = {'low': int(yStr[0]), 'high': int(yStr[1])}


# --- Part One ---
yVelo_max = abs(yCoords['low'])-1

yPos = 0
n = 0
while yVelo_max > 0:
    yPos += yVelo_max
    yVelo_max -= 1
    n += 1
    #print(n, yPos, yVelo_max)
    
result1 = yPos
print(result1)


# --- Part Two ---

def getXidx(velo, limLow, limHigh):
    idxList = []
    if 0 < limHigh and 0 > limLow:
        idxList.append(0)

    pos = 0
    idx = 0
    while velo > 0:
        if pos <= limHigh and pos >= limLow:
            idxList.append(idx)
        pos += velo
        velo -= 1
        idx += 1
    
    return idxList

def getYidx(velo, limLow, limHigh):
    idxList = []
    pos = 0
    idx = 0
    while pos >= limLow:
        if pos >=limLow and pos <= limHigh:
            idxList.append(idx)
        pos += velo
        velo -= 1
        idx += 1

    return idxList

def simulateLaunch(xVelo, xLimLow, xLimHigh, yVelo, yLimLow, yLimHigh):
    xPos = 0
    yPos = 0

    while (xPos <= xLimHigh and xVelo > 0) or (yPos >= yLimLow):
        if xPos <= xLimHigh and xPos >=xLimLow and yPos <= yLimHigh and yPos >=yLimLow:
            return True

        xPos += xVelo
        if xVelo > 0:
            xVelo -= 1
        yPos += yVelo
        yVelo -= 1

    return False

yVelo_max = abs(yCoords['low'])
yVelo_min = int(math.ceil(yCoords['low']))
yVeloSet = {}
for velo in range(yVelo_min, yVelo_max+1):
    idxList = getYidx(velo, yCoords['low'], yCoords['high'])
    if idxList:
        yVeloSet[velo] = idxList

xVeloSet = {}
xVelo_min = math.ceil(math.sqrt(xCoords['high']))
xVelo_max = int(math.ceil(xCoords['high']))+1
for velo in range(xVelo_min, xVelo_max+1):
    idxList = getXidx(velo, xCoords['low'], xCoords['high'])
    if idxList:
        xVeloSet[velo] = idxList

xyVeloList = []
for xv in xVeloSet:
    for yv in yVeloSet:
        if simulateLaunch(xv, xCoords['low'], xCoords['high'], yv, yCoords['low'], yCoords['high']):
            if [xv, yv] not in xyVeloList:
                xyVeloList.append([xv, yv])
                
result2 = len(xyVeloList)
print(result2)
