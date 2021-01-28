if __name__ == "__main__":
    l = sorted([int(i) for i in open("input10.txt", "r").readlines()])
    diff1, diff3, last = 0, 1, 0
    for n in l:
        diff = n - last
        if diff == 1:
            diff1 += 1
        elif diff == 3:
            diff3 += 1
        last = n
    
    print(diff1 * diff3) 
