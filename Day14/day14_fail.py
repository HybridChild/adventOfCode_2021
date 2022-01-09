def most_common(lst):
    return max(set(lst), key=lst.count)

def least_common(lst):
    return min(set(lst), key=lst.count)

def polyGrowthFunc(polyGrowth, pairInsertionList):
    newPolyGrowth = [polyGrowth[0]]
    for i in range(1, len(polyGrowth)):
        for pair in pairInsertionList:
            compPair = ''.join([polyGrowth[i-1], polyGrowth[i]])
            if compPair == pair['pair']:
                newPolyGrowth.append(pair['ins'])
        newPolyGrowth.append(polyGrowth[i])
    return newPolyGrowth


with open('input.txt') as inputFile:
    polyFormula = inputFile.read()

polyFormula = polyFormula.split('\n')
polyFormula.remove('')
polyTemplate = polyFormula.pop(0)

pairInsertionList = []
for pair in polyFormula:
    pair = pair.split(' -> ')
    newPair = {'pair': pair[0], 'ins': pair[1]}
    pairInsertionList.append(newPair)

# --- Part One ---
polyGrowthList = [list(polyTemplate)]
for i in range(0, 10):
    newPolyGrowth = polyGrowthFunc(polyGrowthList[i], pairInsertionList)
    polyGrowthList.append(newPolyGrowth)
    #print(''.join(newPolyGrowth))
    
mostCommon = most_common(newPolyGrowth)
leastCommon = least_common(newPolyGrowth)
result1 = newPolyGrowth.count(mostCommon) - newPolyGrowth.count(leastCommon)
print(result1)

# --- Part Two ---
elemCountList = []
for growth in polyGrowthList:
    newElemCount = [growth.count(mostCommon), growth.count(leastCommon)]
    elemCountList.append(newElemCount)
    #print(newElemCount)

for i in range(1, len(elemCountList)):
    print([elemCountList[i][0] - elemCountList[i-1][0], elemCountList[i][1] - elemCountList[i-1][1]])
