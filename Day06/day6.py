with open('input.txt') as inputFile:
    fishScan = inputFile.read()

fishScan = fishScan.split(',')
fishScan = [int(i) for i in fishScan]

ageCount = [0 for i in range(0, 8+1)]

for fish in fishScan:
    ageCount[fish] += 1

for day in range(0, 80):
    ageCount.append(ageCount.pop(0))
    ageCount[6] += ageCount[8]

print(sum(ageCount))

ageCount = [0 for i in range(0, 8+1)]
for fish in fishScan:
    ageCount[fish] += 1

for day in range(0, 256):
    ageCount.append(ageCount.pop(0))
    ageCount[6] += ageCount[8]

print(sum(ageCount))
