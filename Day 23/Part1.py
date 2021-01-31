def nextDest(curr, temp, low, high):    
    dest = curr
    while True:
        dest = dest - 1 if dest > low else high
        if not dest in temp: return dest

if __name__ == "__main__":
    l = list(open("input.txt", "r").read())
    l = [int(n) for n in l]

    high = max(l)
    low = min(l)
    currentC = 0
    
    for i in range(100):
        temp = []
        current = l[currentC % len(l)]
        for k in range(currentC +1, currentC + 4):
            if currentC < len(l) - 1:
                temp.append(l.pop(currentC + 1))
            else:
                temp.append(l.pop(0))
                
        dest = nextDest(current, temp, low, high)        
        j = l.index(dest)
    
        l = l[:j+1] + temp + l[j+1:] 
        currentC = (l.index(current) + 1) % len(l)
    
    s = ""
    i = l.index(1)
    for j in range(1, len(l)):
        s += str(l[(i+j) % len(l)])
    print(s)
