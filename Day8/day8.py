with open('input.txt') as inputFile:
    inputNotes = inputFile.read()

numSeg = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']

inputNotes = inputNotes.split('\n')
dispList = []
for display in inputNotes:
    display = display.split(' | ')
    display[0] = display[0].split(' ')
    display[1] = display[1].split(' ')
    dispList.append({'sigPat': display[0], 'digVal': display[1]})

# --- Part One ---
result1 = 0
for disp in dispList:
    for num in disp['digVal']:
        if len(num) in [len(numSeg[1]), len(numSeg[4]), len(numSeg[7]), len(numSeg[8])]:
            result1 += 1

print(result1)

# --- Part Two

#   0:      1:      2:      3:      4:
#  aaaa    ....    aaaa    aaaa    ....
# b    c  .    c  .    c  .    c  b    c
# b    c  .    c  .    c  .    c  b    c
#  ....    ....    dddd    dddd    dddd
# e    f  .    f  e    .  .    f  .    f
# e    f  .    f  e    .  .    f  .    f
#  gggg    ....    gggg    gggg    ....

#   5:      6:      7:      8:      9:
#  aaaa    aaaa    aaaa    aaaa    aaaa
# b    .  b    .  .    c  b    c  b    c
# b    .  b    .  .    c  b    c  b    c
#  dddd    dddd    ....    dddd    dddd
# .    f  e    f  .    f  e    f  .    f
# .    f  e    f  .    f  e    f  .    f
#  gggg    gggg    ....    gggg    gggg

def decode7segSignals(sigPat):
    patCode = {}

# 0. From len we know which ones are 1, 4, 7 and 8
    one = [x for x in sigPat if len(x) == 2][0]
    four = [x for x in sigPat if len(x) == 4][0]
    seven = [x for x in sigPat if len(x) == 3][0]
    eight = [x for x in sigPat if len(x) == 7][0]

# 1. find 'a' : Difference between 1 and 7
    patCode['a'] = [x for x in seven if x not in one][0]

# 2. find 'c' : Go through len==6 (0,6,9) and compare to 1. 'c' is missing in one of them (6)
# 3. find 'f' : the one remaining in 1
    for sig in sigPat:
        if len(sig) == 6:
            if one[0] not in sig:
                patCode['c'] = one[0]
                patCode['f'] = one[1]
            elif one[1] not in sig:
                patCode['c'] = one[1]
                patCode['f'] = one[0]

# 4. find 3 : go through len==5, which one includes 'c' and 'f'
    for sig in sigPat:
        if len(sig) == 5:
            if patCode['c'] in sig and patCode['f'] in sig:
                three = sig

# 5. find 'g' : 4+a compared to 3
    for x in three:
        if x not in four and x != patCode['a']:
            patCode['g'] = x

# 6. find 'd' : last unknown in 3
    segs = list(patCode.values())
    for x in three:
        if x not in segs:
            patCode['d'] = x
            segs.append(x)

# 7. find 'b' : last unknown in 4
    for x in four:
        if x not in segs:
            patCode['b'] = x
            segs.append(x)

# 8. find 'e' : last unknown
    for x in eight:
        if x not in segs:
            patCode['e'] = x

    return patCode

def get7segNumber(input, patCode):
    
    numSegDec = []
    for pat in numSeg:
        newPat = ''
        for x in pat:
            newPat += patCode[x]
            newPat = sorted(newPat)

        numSegDec.append(newPat)

    input = sorted(input)

    if input == numSegDec[0]:
        return '0'
    elif input == numSegDec[1]:
        return '1'
    elif input == numSegDec[2]:
        return '2'
    elif input == numSegDec[3]:
        return '3'
    elif input == numSegDec[4]:
        return '4'
    elif input == numSegDec[5]:
        return '5'
    elif input == numSegDec[6]:
        return '6'
    elif input == numSegDec[7]:
        return '7'
    elif input == numSegDec[8]:
        return '8'
    else:
        return '9'
    
result2 = 0

for disp in dispList:
    patCode = decode7segSignals(disp['sigPat'])
    numStr = ''
    for digit in disp['digVal']:
        numStr += get7segNumber(digit, patCode)

    result2 += int(numStr)

print(result2)
