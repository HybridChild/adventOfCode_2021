def traceCaveRecursive(initCave, connList, thisRoute, routeList, smallCave):
    thisRoute.append(initCave)
    if initCave == 'end':
        if thisRoute not in routeList:
            routeList.append(thisRoute)
    else:
        for cave in connList[initCave]:
            if cave != 'start' and cave != initCave:
                if cave.isupper() or cave not in thisRoute or (cave == smallCave and thisRoute.count(smallCave) < 2):
                    nextRoute = thisRoute.copy()
                    traceCaveRecursive(cave, connList, nextRoute, routeList, smallCave)


# Start
with open('input.txt') as inputFile:
    caveMap = inputFile.read()

smallCaveList = []
# List cave connections
caveMap = caveMap.split()
caveConnections = {}
for connection in caveMap:
    connection = connection.split('-')
    for cave in connection:
        if cave not in caveConnections.keys():
            caveConnections[cave] = []
        if cave.islower() and cave != 'start' and cave != 'end' and cave not in smallCaveList:
            smallCaveList.append(cave)
    if connection[0] not in caveConnections[connection[1]]:
        caveConnections[connection[1]].append(connection[0])
    if connection[1] not in caveConnections[connection[0]]:
        caveConnections[connection[0]].append(connection[1])

# Trace cave
routeList = []
newRoute = []
traceCaveRecursive('start', caveConnections, newRoute, routeList, '')

# Part one answer
print(len(routeList))

routeList = []
for smallCave in smallCaveList:
    newRoute = []
    # Slooooooooow
    traceCaveRecursive('start', caveConnections, newRoute, routeList, smallCave)

# Part two answer
print(len(routeList))
