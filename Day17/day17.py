import os

# Start here
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

# PART 1
# Find y velocity
yVel = abs(yCoords['low'])-1

yPos = 0
n = 0
while yVel > 0:
    yPos += yVel
    yVel -= 1
    n += 1
    #print(n, yPos, yVel)
    
result = yPos
print(result)
