import copy

def totalActive(l):
    total = 0
    for w in range(len(l)):
        for z in range(len(l[0])):
            for y in range(len(l[0][0])):
                for x in range(len(l[0][0][0])):
                    total += l[w][z][y][x] == "#"
    return total
    
def checkNeighbours(l, x, y, z, w):
    total = 0
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            for k in range(z - 1, z + 2):
                for m in range(w - 1, w + 2):
                    total += 0 <= i < len(l[0][0][0]) and 0 <= j < len(l[0][0]) and \
                       0 <= k < len(l[0]) and 0<= m <len(l) and (i != x or j != y or k != z or m != w)\
                       and l[m][k][j][i] == "#"
    return total

def processCycle(l):
    temp = copy.deepcopy(l)
    for w in range(len(l)):
        for z in range(len(l[0])):
            for y in range(len(l[0][0])):
                for x in range(len(l[0][0][0])):
                    neighbours = checkNeighbours(l, x, y, z, w)
                    if l[w][z][y][x] == '#' and not (2 <= neighbours <= 3):                            
                        temp[w][z][y][x] = '.'                          
                    elif l[w][z][y][x] == "." and neighbours == 3:                                    
                        temp[w][z][y][x] = '#'     
    return temp

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        l = [line.strip() for line in f]
    
    xrange, yrange = len(l[0]) + 12, len(l) + 12
    xstart, ystart = xrange//2 - len(l[0])//2, yrange//2 - len(l)//2
    xend, yend = xrange//2 + len(l[0])//2, yrange//2 + len(l)//2
    
    grid = []
    for w in range(13):
        grid.append([])
        for z in range(13):
            grid[w].append([])
            for y in range(yrange):
                grid[w][z].append(['.' for x in range(xrange)])
                
    for i in range(xstart, xend):
        for j in range(ystart, yend):
            grid[6][6][j][i] = l[j - ystart][i - xstart]
   
    for i in range(6):
        grid = processCycle(grid)      
             
    print(totalActive(grid))
