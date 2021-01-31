if __name__ == "__main__":
    
    with open("input.txt", "r") as f:
        l = [int(line.strip()) for line in f]
    cKey, dKey = l[0], l[1]
    cLoop, dLoop = 0, 0
    i, curr, n = 1, 1, 7

    while not (cLoop and dLoop):
        curr = (curr * n) % 20201227
        if curr == cKey:
            cLoop = i
        if curr == dKey:
            dLoop = i
        i+=1
    
    n = dKey
    j, curr = 1, 1
    
    while j <= cLoop:
        curr = (curr * n) % 20201227
        j += 1      
    print(curr)     
