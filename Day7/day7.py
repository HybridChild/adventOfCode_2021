import math

with open('input.txt') as inputFile:
    crabList = inputFile.read()

crabList = crabList.split(',')
crabList = [int(x) for x in crabList]
crabList = sorted(crabList)

# --- Part One ---
result1 = 0
middle = crabList[round(len(crabList)/2)]

for crab in crabList:
    result1 += abs(crab-middle)

print(result1)

# --- Part Two ---
result2 = 0
avgPos = math.floor(sum(crabList) / len(crabList))

k = 0
while k < len(crabList):
    cnt = crabList.count(crabList[k])
    add = sum(list(range(1, abs(crabList[k] - avgPos)+1)))
    result2 += add*cnt
    k += cnt

print(result2)
