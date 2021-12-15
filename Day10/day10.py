with open('input.txt') as inputFile:
    navSubSysSyntax = inputFile.read()

navSubSysSyntax = navSubSysSyntax.split()
openChars = ['(', '[', '{', '<']
closeChars = [')', ']', '}', '>']
errorScore = {')': 3, ']': 57, '}': 1197, '>': 25137}
autoScore = {')':1, ']': 2, '}': 3, '>': 4}

def findMatchForClose(line, idx, closed):
    retVal = -1
    if line[idx] in closeChars and idx > 0:
        char = line[idx]
        goalChar = openChars[closeChars.index(char)]
        i = idx -1
        while i > -1:
            if line[i] == goalChar and closed[i] == 0:
                retVal = i
                i = -1
            else:
                i -= 1
    return retVal

# --- Part One ---
lineStatus = []
closedList = []
for line in navSubSysSyntax:
    closed = [0]*len(line)
    fIdx = 0
    bIdx = 0
    failCharIdx = -1
    while fIdx < len(line):
        if line[fIdx] in closeChars:
            bIdx = findMatchForClose(line, fIdx, closed)
            fail = False
            for c in range(bIdx+1, fIdx):
                if closed[c] == 0:
                    fail = True
            
            if fail:
                failCharIdx = fIdx
                fIdx = len(line)
            else:
                closed[bIdx] = 1
                closed[fIdx] = 1

        fIdx += 1
    lineStatus.append(failCharIdx)
    closedList.append(closed)

result1 = 0
i = 0
while i < len(navSubSysSyntax):
    # if line is corrupt
    if lineStatus[i] != -1:
        failChar = navSubSysSyntax[i][lineStatus[i]]
        result1 += errorScore[failChar]    
    i += 1

print(result1)

# --- Part Two ---
def autoComplete(line, closed):
    autoStr = ''
    for i in range(len(line)-1, -1, -1):
        if closed[i] == 0:
            autoStr += closeChars[openChars.index(line[i])]
    return autoStr

def scoreAutoString(autoStr):
    score = 0
    for char in autoStr:
        score *= 5
        score += autoScore[char]
    return score

autoScoreList = []
i = 0
while i < len(navSubSysSyntax):
    # if line is merely incomplete
    if lineStatus[i] == -1:
        autoStr = autoComplete(navSubSysSyntax[i], closedList[i])
        score = scoreAutoString(autoStr)
        autoScoreList.append(score)
    i += 1

autoScoreList = sorted(autoScoreList)


result2 = autoScoreList[int(len(autoScoreList)/2)]
print(result2)
