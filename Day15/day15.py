import queue as PQ
import sys

RISK = 0
POS = 1

def findAdjacent(pos, map):
    adjacent = []
    if pos[0] > 0:
        adjacent.append([pos[0]-1, pos[1]]) ## up
    if pos[0] < len(map)-1:
        adjacent.append([pos[0]+1, pos[1]]) # down
    if pos[1] > 0:
        adjacent.append([pos[0], pos[1]-1]) # left
    if pos[1] < len(map[pos[0]])-1:
        adjacent.append([pos[0], pos[1]+1]) # right

    return adjacent

def traceRoute(riskMap, routePriQue, visitDict):
    currentPos = routePriQue.get()
    adjacent = findAdjacent(currentPos[POS], riskMap)

    for adj in adjacent:
        if str(adj) not in visitDict.keys():
            adjRisk = currentPos[RISK] + riskMap[adj[0]][adj[1]]
            routePriQue.put( [adjRisk, adj] )
            visitDict[str(adj)] = adjRisk
    
    return currentPos

def makeFullRiskMap(riskMap, mapMult):
    fullRiskMap = []
    for r in range(mapMult*len(riskMap)):
        fullRiskMap.append([None]*(mapMult*len(riskMap[0])))
        for c in range(mapMult*len(riskMap[0])):
            if r < len(riskMap):
                if c < len(riskMap[0]):
                    fullRiskMap[r][c] = riskMap[r][c]
                else:
                    val = fullRiskMap[r][c-len(riskMap[0])]+1
                    if val > 9:
                        val = 1
                    fullRiskMap[r][c] = val
            else:
                val = fullRiskMap[r-len(riskMap)][c]+1
                if val > 9:
                    val = 1
                fullRiskMap[r][c] = val

    return fullRiskMap

# --- Start Here ---
# Parse input
with open('input.txt') as inputFile:
    riskMap = inputFile.read().split('\n')

for r in range(len(riskMap)):
    riskMap[r] = list(riskMap[r])
    for c in range(len(riskMap[r])):
        riskMap[r][c] = int(riskMap[r][c])

startPos = [0, 0]

# --- Part One ---
goalPos = [len(riskMap)-1, len(riskMap[0])-1]
currentPos = [0, startPos]  # [RISK, POS]
routePriQue = PQ.PriorityQueue()
routePriQue.put( currentPos )
visitDict = {str(currentPos[POS]): currentPos[RISK]}

while (currentPos[POS] != goalPos) or (len(visitDict.keys()) < len(riskMap)*len(riskMap[0])):
    currentPos = traceRoute(riskMap, routePriQue, visitDict)

print('Part One result: ', visitDict[str(goalPos)])

# --- Part Two ---
routePriQue.empty()
currentPos = [0, startPos]  # [RISK, POS]
routePriQue.put( currentPos )
visitDict.clear()

mapMult = 5
fullRiskMap = makeFullRiskMap(riskMap, mapMult)
goalPos = [len(fullRiskMap)-1, len(fullRiskMap[0])-1]

while (currentPos[POS] != goalPos) or (len(visitDict.keys()) < len(fullRiskMap)*len(fullRiskMap[0])):
    currentPos = traceRoute(fullRiskMap, routePriQue, visitDict)

print('Part Two result: ', visitDict[str(goalPos)])
