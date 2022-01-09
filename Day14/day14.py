from collections import Counter

with open('input.txt') as inputFile:
    polyTemplate, tmpRules = inputFile.read().split('\n\n')

tmpRules = tmpRules.split('\n')
pairInsertionRules = {}
for rule in tmpRules:
    pairInsertionRules[rule[0:2]] = {'elem': rule[len(rule)-1],
                                     'pair1': ''.join([rule[0], rule[len(rule)-1]]),
                                     'pair2': ''.join([rule[len(rule)-1], rule[1]])}

# Count pairs of elements in polymer, return as dictionary
def countPairs(polymer):
    pairCount = Counter()
    for i in range(1, len(polymer)):
        pair = polymer[i-1:i+1]
        if pair not in pairCount.keys():
            pairCount[pair] = 1
        else:
            pairCount[pair] += 1
    return pairCount

def countElements(polymer):
    return Counter(polymer)

def growNewPolymer(pairCount, rules, elemCnt):
    newPairCount = {}
    for pair, count in pairCount.items():
        if pair in rules.keys():
            pair1 = rules[pair]['pair1']
            pair2 = rules[pair]['pair2']
            elem = rules[pair]['elem']

            if elem not in elemCnt.keys():
                elemCnt[elem] = count
            else:
                elemCnt[elem] += count

            if pair1 not in newPairCount.keys():
                newPairCount[pair1] = count
            else:
                newPairCount[pair1] += count

            if pair2 not in newPairCount.keys():
                newPairCount[pair2] = count
            else:
                newPairCount[pair2] += count

    return newPairCount


def polymerGrowth(poly, rules, iterations):
    pairCount = countPairs(poly)
    elemCount = countElements(poly)
    for i in range(iterations):
        pairCount = growNewPolymer(pairCount, rules, elemCount)
    result = sorted(elemCount.values())
    return result[-1] - result[0]

result1 = polymerGrowth(polyTemplate, pairInsertionRules, iterations=10)
result2 = polymerGrowth(polyTemplate, pairInsertionRules, iterations=40)

print(result1)
print(result2)
