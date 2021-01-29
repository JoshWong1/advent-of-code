if __name__ == "__main__":
    l = open("input.txt", "r").read().strip().split(",")   
    d = {}
    
    for i,n in enumerate(l):
        d[int(n)] = i
    last = l[i]
    
    while True:    
        if i == 2019:
            print(last)
            break        
        if not last in d:
            d[last] = i
            last = 0
        else:
            temp = i - d[last]
            d[last] = i
            last = temp
        i += 1
