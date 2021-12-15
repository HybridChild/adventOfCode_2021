def findAdjacent(r, c, map):
    adjacent = {}
    findUp(r, c, map, adjacent)
    findUpRight(r, c, map, adjacent)
    findRight(r, c, map, adjacent)
    findDownRight(r, c, map, adjacent)
    findDown(r, c, map, adjacent)
    findDownLeft(r, c, map, adjacent)
    findLeft(r, c, map, adjacent)
    findUpLeft(r, c, map, adjacent)
    return adjacent

def findUp(r, c, map, adj):
    if r > 0:
        adj['up'] = map[r-1][c]
    else:
        adj.pop('up', None)

def findUpRight(r, c, map, adj):
    if r > 0 and c < len(map[r])-1:
        adj['upRight'] = map[r-1][c+1]
    else:
        adj.pop('upRight', None)

def findRight(r, c, map, adj):
    if c < len(map[r])-1:
        adj['right'] = map[r][c+1]
    else:
        adj.pop('right', None)

def findDownRight(r, c, map, adj):
    if r < len(map)-1 and c < len(map[r])-1:
        adj['downRight'] = map[r+1][c+1]
    else:
        adj.pop('downRight', None)

def findDown(r, c, map, adj):
    if r < len(map)-1:
        adj['down'] = map[r+1][c]
    else:
        adj.pop('down', None)

def findDownLeft(r, c, map, adj):
    if r < len(map)-1 and c > 0:
        adj['downLeft'] = map[r+1][c-1]
    else:
        adj.pop('downLeft', None)

def findLeft(r, c, map, adj):
    if c > 0:
        adj['left'] = map[r][c-1]
    else:
        adj.pop('left', None)

def findUpLeft(r, c, map, adj):
    if c > 0 and r > 0:
        adj['upLeft'] = map[r-1][c-1]
    else:
        adj.pop('upLeft', None)

def flashAllRound(map, flashMap):
    notDone = True
    while notDone:
        notDone = False
        for r in range(0, len(map)):
            for c in range(0, len(map[r])):
                if map[r][c] > 9 and flashMap[r][c] == 0:
                    notDone = True
                    flashMap[r][c] = 1
                    adjacent = findAdjacent(r, c, map)
                    if 'up' in adjacent.keys():
                        map[r-1][c] += 1
                    if 'upRight' in adjacent.keys():
                        map[r-1][c+1] += 1
                    if 'right' in adjacent.keys():
                        map[r][c+1] += 1
                    if 'downRight' in adjacent.keys():
                        map[r+1][c+1] += 1
                    if 'down' in adjacent.keys():
                        map[r+1][c] += 1
                    if 'downLeft' in adjacent.keys():
                        map[r+1][c-1] += 1
                    if 'left' in adjacent.keys():
                        map[r][c-1] += 1
                    if 'upLeft' in adjacent.keys():
                        map[r-1][c-1] += 1


def charge(energyMap):
    for r in range(0, len(energyMap)):
        for c in range(0, len(energyMap[0])):
            energyMap[r][c] += 1

def flash(map):
    flashMap = [[0 for item in range(len(map))] for item in range(len(map))]
    flashAllRound(map, flashMap)

def clearFlash(map):
    flashCnt = 0
    for r in range(0, len(map)):
        for c in range(0, len(map[0])):
            if map[r][c] > 9:
                map[r][c] = 0
                flashCnt += 1
    return flashCnt
    

with open('input.txt') as inputFile:
    OctoEnergy = inputFile.read()

OctoEnergy = OctoEnergy.split()
# convert to integers
i = 0
while i < len(OctoEnergy):
    newRow = []
    for x in OctoEnergy[i]:
        newRow.append(int(x))
    OctoEnergy[i] = newRow
    i += 1

flashAccum = 0
idx = 0
flashMap = [[0 for item in range(len(OctoEnergy))] for item in range(len(OctoEnergy))]
allFlash = False
while not allFlash:
    charge(OctoEnergy)
    flash(OctoEnergy)
    flashAccum += clearFlash(OctoEnergy)
    if idx == 99:
        print(flashAccum)   # Part One answer
    if OctoEnergy == flashMap:
        allFlash = True
    idx += 1

print(idx)  # Part Two answer
