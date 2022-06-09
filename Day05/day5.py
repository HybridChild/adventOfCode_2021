with open('input.txt') as inputFile:
    ventMap = inputFile.read()

ventMap = ventMap.split('\n')
ventMap.remove('')

for i in range(0, len(ventMap)):
    ventMap[i] = ventMap[i].split(' -> ')
    ventMap[i][0] = ventMap[i][0].split(',')
    ventMap[i][1] = ventMap[i][1].split(',')
    ventMap[i][0][0] = int(ventMap[i][0][0])
    ventMap[i][0][1] = int(ventMap[i][0][1])
    ventMap[i][1][0] = int(ventMap[i][1][0])
    ventMap[i][1][1] = int(ventMap[i][1][1])

# find largest coordinate
mapSize = 0
for line in ventMap:
    for coord in line:
        for xy in coord:
            if xy > mapSize:
                mapSize = xy

ventDiagram = [[0 for i in range(mapSize+1)] for j in range(mapSize+1)]

# --- Part One ---
for line in ventMap:
    if line[0][0] == line[1][0]:    # vertical lines
        lo = min([line[0][1], line[1][1]])
        hi = max([line[0][1], line[1][1]])
        for y in range(lo, hi+1):
            ventDiagram[line[0][0]][y] += 1
    elif line[0][1] == line[1][1]:    # horizontal lines
        lo = min([line[0][0], line[1][0]])
        hi = max([line[0][0], line[1][0]])
        for x in range(lo, hi+1):
            ventDiagram[x][line[0][1]] += 1



overlaps = 0
for x in range(0, mapSize+1):
    for y in range(0, mapSize+1):
        if ventDiagram[x][y] > 1:
            overlaps += 1

print(overlaps)

# --- Part Two ---
for line in ventMap:
    if line[0][0] != line[1][0] and line[0][1] != line[1][1]:
        xAdd = 1 if line[0][0] < line[1][0] else -1
        yAdd = 1 if line[0][1] < line[1][1] else -1
        katLen = max([line[0][0], line[1][0]]) - min([line[0][0], line[1][0]])
        for i in range(0, katLen+1):
            x = line[0][0] + (xAdd * i)
            y = line[0][1] + (yAdd * i)
            ventDiagram[x][y] += 1

overlaps = 0
for x in range(0, mapSize+1):
    for y in range(0, mapSize+1):
        if ventDiagram[x][y] > 1:
            overlaps += 1

print(overlaps)
