with open('input.txt', 'r') as inputFile:
    sweepReport = inputFile.read()

sweepReport = sweepReport.split()
sweepReport = [int(i) for i in sweepReport] # use list comprehension to convert to integers 

result1 = 0
result2 = 0
for i in range(1, len(sweepReport)):
    if sweepReport[i] > sweepReport[i-1]:
        result1 += 1

    if i > 2:
        win1 = sweepReport[i-3:i]
        win2 = sweepReport[i-2:i+1]
        if sum(win2) > sum(win1):
            result2 += 1

print(result1)
print(result2)
