# Get data from input file
with open("input.txt", "r") as inputFile: 
    coursePlan = inputFile.read()

coursePlan = coursePlan.split('\n')
coursePlan.remove('')
instList = []

for inst in coursePlan:
    inst = inst.split(' ')
    instList.append({'Command': inst[0], 'Value': int(inst[1])})

dest1 = {'Depth': 0, 'Position': 0}
dest2 = {'Depth': 0, 'Position': 0, 'Aim': 0}

for inst in instList:
    if inst['Command'] == 'forward':
        dest1['Position'] += inst['Value']
        dest2['Position'] += inst['Value']
        dest2['Depth'] += ( dest2['Aim'] * inst['Value'] )
    elif inst['Command'] == 'down':
        dest1['Depth'] += inst['Value']
        dest2['Aim'] += inst['Value']
    elif inst['Command'] == 'up':
        dest1['Depth'] -= inst['Value']
        dest2['Aim'] -= inst['Value']

print(dest1['Depth'] * dest1['Position'])
print(dest2['Depth'] * dest1['Position'])
