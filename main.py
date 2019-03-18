from time import sleep
import numpy as np
import matplotlib.pyplot as plt

f = open('c_medium.in', 'r')

solution = []
check = set()

vars = f.readline().split(' ')
R = int(vars[0])
C = int(vars[1])
L = int(vars[2])
H = int(vars[3].strip('\n'))

sum_min = L

# MEDIUM
# types = {0: (12, 1), 1: (6, 2), 2: (4, 3), 3: (3, 4), 4: (2, 6), 5: (1, 12), 6: (10, 1), 7: (5, 2), 8: (2, 5), 9: (1, 10), 10: (8, 1), 11: (4, 2), 12: (2, 4), 13: (1, 8)}
types = {0: (12, 1), 1: (11, 1), 2: (10, 1), 3: (9, 1), 4: (8, 1), 5: (6, 2), 6: (5, 2), 7: (4, 2), 8: (4, 3), 9: (3, 4), 10: (2, 4), 11: (2, 5), 12: (2, 6), 13: (1, 8), 14: (1, 9), 15: (1, 10), 16: (1, 11), 17: (1, 12)}
# LARGE
#types = {0: (14, 1), 1: (7, 2), 2: (2, 7), 3: (1, 14), 4: (12, 1), 5: (6, 2), 6: (4, 3), 7: (3, 4), 8: (2, 6), 9: (1, 12)}
# SMULL!
# types = {0: (5, 1), 1: (1, 5), 2: (4, 1), 3: (1, 4), 4: (3, 1), 5: (1, 3), 6: (2, 1), 7: (1, 2)}

pizza = [[char for char in line.strip('\n')] for line in f.readlines()]

for i in range(len(pizza)):
    for j in range(len(pizza[0])):
        if pizza[i][j] == 'T':
            pizza[i][j] = 1
        else:
            pizza[i][j] = 0

pizza = np.array(pizza)

f.close()


def isValid(x1, y1, x2, y2, btype):
    #if (x1, y1, x2, y2, btype) in check:
    #    return False
    if x2 >= C or y2 >= R:
        return False
    # print(x1, y1, x2, y2, btype)
    sum_max = (x2-x1+1) * (y2-y1+1) - L
    # print("sum_max:", sum_max)
    if x2 > C or y2 > R:
        return False
    section = pizza[y1:y2+1, x1:x2+1]
    sum = np.sum(section)
    #if (sum_min <= sum <= sum_max) and (section.max() < 2):
        #print(x1, y1, x2, y2, "Block is valid")
    return (sum_min <= sum <= sum_max) and (section.max() < 2)


def isReady():
    for elem in pizza[:,-1]:
        if elem < 2:
            return False
    return True


def startPoint():
    for y in range(R):
        for x in range(C):
            if pizza[y,x] < 2:
                #print(x,y)
                return (x,y)
    return None


def placeBlock(x1, y1, x2, y2, btype):
    # print("placing block", x1, y1 ,x2 , y2, btype)
    pizza[y1:y2+1, x1:x2+1] += (10+btype*5)
    solution.append([x1, y1, x2, y2, btype])
    check.add((x1, y1, x2, y2, btype))

    

    plt.imshow(pizza)
    plt.colorbar()

    plt.show(block=False)
    plt.pause(.001)
    plt.clf()




def deleteBlock():
    x1, y1, x2, y2, btype = solution[-1][:]
    # print("deleting block", x1, y1 ,x2 , y2, btype)
    # print(pizza[(y1-5):(y2+5), (x1-5):(x2+5)])
    pizza[y1:y2 + 1, x1:x2 + 1] -= (10+btype*5)

    del solution[-1]

    plt.imshow(pizza)
    plt.colorbar()

    plt.show(block=False)
    plt.pause(0.001)
    plt.clf()



def backtrack():
    # print("Backtracking...")
    # print(len(solution))

    # plt.imshow(pizza)
    # plt.colorbar()
    # plt.show()
    try:
        x1, y1, x2, y2, btype = solution[-1]
    except:
        print(pizza[:25, :25])
        exit()
    deleteBlock()
    for newtype in range(btype+1, len(types)):
        if isValid(x1, y1, types[newtype][0]+x1-1, types[newtype][1]+y1-1, newtype):
            #print("found new valid block")
            placeBlock(x1, y1, types[newtype][0]+x1-1, types[newtype][1]+y1-1, newtype)
            return
    backtrack()
    return





while not isReady():
    x, y = startPoint()
    #print("start point:", x,y)
    isPlaced = False
    for btype in range(len(types)):
        #print("btype", btype)
        if isValid(x, y, types[btype][0]+x-1, types[btype][1]+y-1, btype):
            placeBlock(x, y, types[btype][0]+x-1, types[btype][1]+y-1, btype)
            isPlaced = True
            break
    # plt.imshow(pizza)
    # plt.colorbar()
    # plt.show()
    if not isPlaced:
        backtrack()

f = open('solution.txt', 'w')

f.write(str(len(solution))+'\n')
for i in range(len(solution)):
    for j in range(len(solution[i])-1):
        f.write(str(solution[i][j])+ ' ')
    f.write('\n')
f.close()

plt.imshow(pizza)
plt.colorbar()
plt.show()
print(len(solution))
