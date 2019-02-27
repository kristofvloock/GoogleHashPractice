f = open('a_example.in', 'r')
solution = []

pizza = [[char for char in line.strip('\n')] for line in f.readlines()[1:]]

for i in range(len(pizza)):
    for j in range(len(pizza[0])):
        if pizza[i][j] == 'T':
            pizza[i][j] = 1
        else:
            pizza[i][j] = 0

def isValid(coords):


print(pizza)
