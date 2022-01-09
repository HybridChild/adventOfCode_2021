def foldFunc(dotList, foldInst):
    newDotList = []
    for dot in dotList:
        if foldInst['dir'] == 'x':  # horizontal (up) hold
            if dot[0] > foldInst['dist']:
                row = foldInst['dist'] - (dot[0] - foldInst['dist'])
                newDot = [row, dot[1]]
                if newDot not in newDotList:
                    newDotList.append(newDot)
            elif dot[0] < foldInst['dist']:
                if dot not in newDotList:
                    newDotList.append(dot)
        
        elif foldInst['dir'] == 'y':    # vertical (left) fold
            if dot[1] > foldInst['dist']:
                col = foldInst['dist'] - (dot[1] - foldInst['dist'])
                newDot = [dot[0], col]
                if newDot not in newDotList:
                    newDotList.append(newDot)
            elif dot[1] < foldInst['dist']:
                if dot not in newDotList:
                    newDotList.append(dot)

    return newDotList


def printDots(dotList):
    xLen = 0
    yLen = 0
    for dot in dotList:
        if dot[0] > xLen:
            xLen = dot[0]
        if dot[1] > yLen:
            yLen = dot[1]

    line = []
    page = []
    for i in range(0, xLen+1):
        line.append('.')
    for i in range(0, yLen+1):
        newLine = line.copy()
        page.append(newLine)

    for dot in dotList:
        page[dot[1]][dot[0]] = '#'

    for line in page:
        line = ''.join(line)
        print(line)





with open('input.txt') as inputFile:
    transPaper = inputFile.read()

transPaper = transPaper.split('\n')
transPaper.remove('')

dotList = [x for x in transPaper if 'fold along' not in x]
i = 0
for dot in dotList:
    dot = dot.split(',')
    dot[0] = int(dot[0])
    dot[1] = int(dot[1])
    dotList[i] = dot
    i += 1
dotList = sorted(dotList)

foldList = [x for x in transPaper if 'fold along' in x]
i = 0
for fold in foldList:
    newFold = {}
    fold = fold[11: len(fold)]
    fold = fold.split('=')
    newFold['dir'] = fold[0]
    newFold['dist'] = int(fold[1])
    foldList[i] = newFold
    i += 1

# --- Part One ---
newDotList = [dotList]
foldCnt = 0
for fold in foldList:
    newestDotList = foldFunc(newDotList[foldCnt], fold)
    newDotList.append(newestDotList)
    foldCnt += 1

result1 = len(newDotList[1])
print(result1)

# --- Part Two ---
printDots(newestDotList)

#    ####.###..#..#.####.#....###..###..###.
#    #....#..#.#..#.#....#....#..#.#..#.#..#
#    ###..#..#.#..#.###..#....#..#.###..#..#
#    #....###..#..#.#....#....###..#..#.###.
#    #....#....#..#.#....#....#....#..#.#.#.
#    ####.#.....##..####.####.#....###..#..#
