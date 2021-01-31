import copy

def totalActive(l):
    total = 0
    for z in range(len(l)):
        for y in range(len(l[0])):
            for x in range(len(l[0][0])):
                total += l[z][y][x] == "#"
    return total
    
def checkNeighbours(l, x, y, z):
    total = 0
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            for k in range(z - 1, z + 2):
                total += 0 <= i < len(l[0][0]) and 0 <= j < len(l[0]) and 0 <= k < len(l) \
                   and (i != x or j != y or k != z) and l[k][j][i] == "#"                   
    return total

def processCycle(l):
    temp = copy.deepcopy(l)
    for z in range(len(l)):
        for y in range(len(l[0])):
            for x in range(len(l[0][0])):
                if l[z][y][x] == '#' and not(2 <= checkNeighbours(l, x, y, z) <= 3):
                    temp[z][y][x] = '.'
                   
                elif l[z][y][x] == "." and checkNeighbours(l, x, y, z) == 3:
                    temp[z][y][x] = '#'                     
    return temp
                    
                
if __name__ == "__main__":
    with open("input.txt", "r") as f:
        l = [line.strip() for line in f]    
    
    xrange, yrange = len(l[0]) + 12, len(l) + 12
    xstart, ystart = xrange//2 - len(l[0])//2, yrange//2 - len(l)//2
    xend, yend = xrange//2 + len(l[0])//2, yrange//2 + len(l)//2

    grid = []
    for z in range(0, 13):
        grid.append([])
        for y in range(0, yrange + 1):
            grid[z].append(['.' for x in range(xrange +1)])
    for i in range(xstart, xend):
        for j in range(ystart, yend):
            grid[6][j][i] = l[j - ystart][i - xstart]
            
    for i in range(6):
        grid = processCycle(grid)
    
    print(totalActive(grid))
