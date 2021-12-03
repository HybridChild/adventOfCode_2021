def countBits(inList, index):
    result = {'Ones': [], 'Zeros': []}

    for i in range(0, len(inList)):
        if index < len(inList[i]):
            if inList[i][index] == '1':
                result['Ones'].append(i)
            else:
                result['Zeros'].append(i)

    return result

# Get data from input file
with open('input.txt', 'r') as inputFile:
    diagReport = inputFile.read()

diagReport = diagReport.split('\n')
diagReport.remove('')
bitCnt = len(diagReport[0])

# Part 1
gamma = 0
epsilon = 0

for i in range(0, bitCnt):
    bits = countBits(diagReport, i)

    if len(bits['Ones']) > (len(diagReport) / 2):
        gamma += pow(2, bitCnt-1-i)
    else:
        epsilon += pow(2, bitCnt-1-i)

power = gamma * epsilon
print(power)

# Part 2
oxyList = diagReport
CO2List = diagReport

for i in range(0, bitCnt):
    if len(oxyList) > 1:
        oxyBits = countBits(oxyList, i)

        if len(oxyBits['Ones']) >= len(oxyBits['Zeros']):
            oxyList = [v for idx, v in enumerate(oxyList) if idx not in oxyBits['Zeros']]
        else:
            oxyList = [v for idx, v in enumerate(oxyList) if idx not in oxyBits['Ones']]

    if len(CO2List) > 1:
        CO2Bits = countBits(CO2List, i)

        if len(CO2Bits['Zeros']) <= len(CO2Bits['Ones']):
            CO2List = [v for idx, v in enumerate(CO2List) if idx not in CO2Bits['Ones']]
        else:
            CO2List = [v for idx, v in enumerate(CO2List) if idx not in CO2Bits['Zeros']]

oxygenGen = int(oxyList[0], 2)
CO2Scrub = int(CO2List[0], 2)

print(oxygenGen*CO2Scrub)
