with open('input.txt', 'r') as inputFile:
    bingoBoard = inputFile.read()

bingoBoard = bingoBoard.split('\n')
bingoBoard = [x for x in bingoBoard if x != '']
for i in range(0, len(bingoBoard)):
    bingoBoard[i] = bingoBoard[i].split(' ')
    bingoBoard[i] = [x for x in bingoBoard[i] if x != '']

drawList = bingoBoard.pop(0)
drawList = drawList[0].split(',')

for i in range(0, len(drawList)):
    drawList[i] = int(drawList[i])

for i in range(0, len(bingoBoard)):
    for k in range(0, len(bingoBoard[i])):
        bingoBoard[i][k] = int(bingoBoard[i][k])

boardList = []
markCntList = []
for i in range(0, int(len(bingoBoard)/5)):
    boardList.append(bingoBoard[i*5:i*5+5])
    markCntList.append({'rows': [0, 0, 0, 0, 0], 'cols': [0, 0, 0, 0, 0]})

for i in range(0, len(boardList)):
    for r in range(0, 5):
        for c in range(0, 5):
            boardList[i][r][c] = {'num': boardList[i][r][c], 'mark': False}

# --- Part One ---
winBoard = {'board': -1, 'row': -1, 'col': -1, 'draw': -1, 'score': -1}
drawCnt = 0
while winBoard['board'] == -1 and drawCnt < len(drawList):
    b = 0
    while b < len(boardList):
        r = 0
        while r < 5:
            c = 0
            while c < 5:
                if boardList[b][r][c]['num'] == drawList[drawCnt]:
                    boardList[b][r][c]['mark'] = True
                    markCntList[b]['rows'][r] += 1
                    markCntList[b]['cols'][c] += 1

                    if markCntList[b]['rows'][r] == 5:
                        winBoard['board'] = b
                        winBoard['row'] = r
                        winBoard['draw'] = drawList[drawCnt]
                    elif markCntList[b]['cols'][c] == 5:
                        winBoard['board'] = b
                        winBoard['col'] = c
                        winBoard['draw'] = drawList[drawCnt]
                    
                    if winBoard['board'] != -1:
                        c = 5
                        r = 5
                        b = len(boardList)
    
                c += 1
            r += 1
        b += 1
    drawCnt += 1

markSum = 0
for r in range(0, 5):
    for c in range(0, 5):
        if boardList[winBoard['board']][r][c]['mark'] != True:
            markSum += boardList[winBoard['board']][r][c]['num']

winBoard['score'] = markSum * winBoard['draw']
print(winBoard['score'])

# --- Part Two ---
for i in range(0, len(markCntList)):
    for rc in range(0, 5):
        markCntList[i]['rows'][rc] = 0
        markCntList[i]['cols'][rc] = 0

boardCountDownList = list(range(0, len(boardList)))

finalDraw = 0
drawCnt = 0
while drawCnt < len(drawList):
    b = 0
    while b < len(boardList):
        r = 0
        while r < 5:
            c = 0
            while c < 5:
                if boardList[b][r][c]['num'] == drawList[drawCnt]:
                    boardList[b][r][c]['mark'] = True
                    markCntList[b]['rows'][r] += 1
                    markCntList[b]['cols'][c] += 1

                    if (markCntList[b]['rows'][r] == 5 or markCntList[b]['cols'][c] == 5) and (b in boardCountDownList) :
                        c = 5
                        r = 5

                        if len(boardCountDownList) > 1:
                            boardCountDownList.remove(b)
                        else:
                            finalDraw = drawList[drawCnt]
                            b = len(boardList)
                            drawCnt = len(drawList)

                c += 1
            r += 1
        b += 1
    drawCnt += 1

markSum = 0
for r in range(0, 5):
    for c in range(0, 5):
        if boardList[boardCountDownList[0]][r][c]['mark'] != True:
            markSum += boardList[boardCountDownList[0]][r][c]['num']

lastScore = markSum * finalDraw
print(lastScore)
