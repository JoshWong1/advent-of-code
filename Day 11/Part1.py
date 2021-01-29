import copy

def numOccupied(l):
    s = 0
    for i in range(0, len(l)):
        for j in range(0, len(l[0])):
            if l[i][j] == "#":
                s += 1                    
    return s

def occupiable(l, i, j):
    adjacent = [(i+1, j), (i, j+1), (i-1, j), (i, j-1), (i+1,j+1), (i+1, j-1), \
                (i-1, j+1), (i-1, j-1)]    
    for (i2, j2) in adjacent:
        if 0 <= i2 < len(l) and 0 <= j2 < len(l[0]) and l[i2][j2] == "#":
            return False                                                                 
    return True         

def leave(l, i, j):
    adjacent = [(i+1, j), (i, j+1), (i-1, j), (i, j-1), (i+1,j+1), (i+1, j-1), \
                (i-1, j+1), (i-1, j-1)]
    s = 0
    for (i2, j2) in adjacent:
        if 0 <= i2 < len(l) and 0 <= j2 < len(l[0]) and l[i2][j2] == "#":
            s += 1
            if s >= 4:
                return True
    return False
                                
if __name__ == "__main__":

    l = [list(line.strip()) for line in open("input.txt", "r").readlines()]
    last = 0
    k = True
    while True:
        l2 = copy.deepcopy(l)
        for i, s in enumerate(l):
            for j, c in enumerate(s):
                if k and c == 'L' and occupiable(l, i, j):
                    l2[i][j] = '#'
                elif not k and c == '#' and leave(l, i, j):
                    l2[i][j] = 'L'
        n = numOccupied(l2)
        if last == n:
            print(n)
            break
        last = n
        l = l2
        k = not k
