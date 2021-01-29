import copy

def numOccupied(l):
    s = 0
    for row in l:
        for seat in row:
            if seat == "#": s += 1                    
    return s

def occupiable(l, i, j):
    dirs = {(0, 1), (0, -1), (1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1)}
    for d in dirs:
        if check(l, i, j, d):
            return False
    return True

def leave(l, i, j):
    dirs = {(0, 1), (0, -1), (1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1)}
    count = 0
    for d in dirs:
        count += check(l, i, j, d)         
        if count >= 5:
            return True        
    return False

def check(l, i, j, d):
    incr1, incr2 = d
    i, j = i + incr1, j + incr2
    while 0 <= i < len(l) and 0 <= j < len(l[0]) and l[i][j] != 'L':
        if l[i][j] == '#':
            return 1
        i, j = i + incr1, j + incr2
    return 0
   
                                
if __name__ == "__main__":
    l = [list(line.strip()) for line in open("input11.txt", "r").readlines()]
    last = 0
    k = True
    while True:
        l2 = copy.deepcopy(l)
        for i, row in enumerate(l):
            for j, seat in enumerate(row):
                if k and seat == "L" and occupiable(l, i, j):
                    l2[i][j] = "#"
                elif not k and seat == "#" and leave(l, i, j):
                    l2[i][j] = "L"
        n = numOccupied(l2)
        if last == n:            
            print(n)
            break
        last = n
        l = l2
        k = not k
