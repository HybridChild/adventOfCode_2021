
def findLowPoints(map):
    lowPts = []
    for r in range(0, len(map)):
        for c in range(0, len(map[0])):
            pt = [r, c]
            adjacent = findAdjacent(pt, map)
            if map[r][c] < min(adjacent.values()):
                lowPts.append([r, c])
            c += 1
        r += 1
    return lowPts

def findAdjacent(pt, map):
    r = pt[0]
    c = pt[1]
    adjacent = {}
    findUp([r, c], map, adjacent)
    findDown([r, c], map, adjacent)
    findLeft([r, c], map, adjacent)
    findRight([r, c], map, adjacent)
    return adjacent

def findUp(pt, map, adj):
    r = pt[0]
    c = pt[1]
    if r > 0:
        adj['up'] = map[r-1][c]
    else:
        adj.pop('up', None)

def findDown(pt, map, adj):
    r = pt[0]
    c = pt[1]
    if r < len(map)-1:
        adj['down'] = map[r+1][c]
    else:
        adj.pop('down', None)

def findLeft(pt, map, adj):
    r = pt[0]
    c = pt[1]
    if c > 0:
        adj['left'] = map[r][c-1]
    else:
        adj.pop('left', None)

def findRight(pt, map, adj):
    r = pt[0]
    c = pt[1]
    if c < len(map[0])-1:
        adj['right'] = map[r][c+1]
    else:
        adj.pop('right', None)

def calculateRisk(lp, map):
    return map[lp[0]][lp[1]] + 1

def findBasin(lp, map):
    basin = [lp]

    adjacent = findAdjacent(lp, map)

    # evaluate up
    step = 1
    pt = lp
    while 'up' in adjacent.keys():
        if adjacent['up'] > map[pt[0][pt[1]]]:
            pt = [pt[0]-step][pt[1]]
            basin.append(pt)
        findUp(pt, map, adjacent)
        step += 1

def traceBasin(initPt, map, dir, basin):
    thisVal = int(map[initPt[0]][initPt[1]])
    if initPt not in basin:
        basin.append(initPt)

    adjacent = findAdjacent(initPt, map)

    if dir != 'up' and 'up' in adjacent.keys():
        if int(adjacent['up']) > thisVal and int(adjacent['up']) != 9:
            nexPt = [initPt[0]-1, initPt[1]]
            traceBasin(nexPt, map, 'down', basin)
    if dir != 'right' and 'right' in adjacent.keys():
        if int(adjacent['right']) > thisVal and int(adjacent['right']) != 9:
            nexPt = [initPt[0], initPt[1]+1]
            traceBasin(nexPt, map, 'left', basin)
    if dir != 'down' and 'down' in adjacent.keys():
        if int(adjacent['down']) > thisVal and int(adjacent['down']) != 9:
            nexPt = [initPt[0]+1, initPt[1]]
            traceBasin(nexPt, map, 'up', basin)
    if dir != 'left' and 'left' in adjacent.keys():
        if int(adjacent['left']) > thisVal and int(adjacent['left']) != 9:
            nexPt = [initPt[0], initPt[1]-1]
            traceBasin(nexPt, map, 'right', basin)



with open('input.txt') as inputFile:
    map = inputFile.read()

map = map.split()
# convert to integers
intMap = []
for r in range(0, len(map)):
    intRow = []
    for c in range(0, len(map[r])):
        intRow.append(int(map[r][c]))
    intMap.append(intRow)

# --- Part One ---
lowPointList = findLowPoints(intMap)
riskSum = 0
for lp in lowPointList:
    riskSum += calculateRisk(lp, intMap)

print(riskSum)

# --- Part Two ---
basinList = []
i = 0
for lp in lowPointList:
    basinList.append([])
    traceBasin(lp, map, 'none', basinList[i])
    i += 1


xlBasin = []
for i in range(0, 3):
    biggest = max(basinList, key=len)
    idx = basinList.index(biggest)
    xlBasin.append(basinList.pop(idx))

result2 = len(xlBasin[0]) * len(xlBasin[1]) * len(xlBasin[2])
print(result2)
