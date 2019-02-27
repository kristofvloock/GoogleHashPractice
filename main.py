import numpy as np

f = open('a_example.in', 'r')

solution = []

vars = f.readline().split(' ')
R = int(vars[0])
C = int(vars[1])
L = int(vars[2])
H = int(vars[3].strip('\n'))

sum_min = L
sum_max = H - L

types = {0: (14, 1), 1: (7, 2), 2: (2, 7), 3: (1, 14), 4: (12, 1), 5: (6, 2), 6: (4, 3), 7: (3, 4), 8: (2, 6), 9: (1, 12)}

pizza = [[char for char in line.strip('\n')] for line in f.readlines()]

for i in range(len(pizza)):
    for j in range(len(pizza[0])):
        if pizza[i][j] == 'T':
            pizza[i][j] = 1
        else:
            pizza[i][j] = 0

pizza = np.array(pizza)


def isValid(x1, y1, x2, y2):
    section = pizza[x1:x2+1,y1:y2+1]
    sum = np.sum(section)
    return (sum_min <= sum <= sum_max) and (section.max() < 2)


def isReady():
    for elem in pizza[:,-1]:
        if elem < 2:
            return False
    return True


def startPoint():
    for y in range(R):
        for x in range(C):
            if pizza[x,y] != 2:
                return (x,y)
    return None


def placeBlock(x1, y1, x2, y2, btype):
    pizza[x1:x2+1, y1:y2+1] + 2
    solution.append([x1, y1, x2, y2, btype])


def deleteBlock():
    x1, x2, y1, y2, btype = solution[-1]
    pizza[x1:x2 + 1, y1:y2 + 1] - 2
    del solution[-1]


def backtrack():
    x1, x2, y1, y2, btype = solution[-1]
    deleteBlock()
    for newtype in range(btype+1, len(types)):
        if isValid(x, y, types[btype][0]+x-1, types[btype][1]+y-1):
            placeBlock(x, y, types[btype][0]+x-1, types[btype][1]+y-1)
            return
    backtrack()


while not isReady():
    x, y = startPoint()
    isPlaced = False
    for btype in types.keys():
        if isValid(x, y, types[btype][0]+x-1, types[btype][1]+y-1):
            placeBlock(x, y, types[btype][0]+x-1, types[btype][1]+y-1)
            isPlaced = True
            break
    if not isPlaced:
        backtrack()


