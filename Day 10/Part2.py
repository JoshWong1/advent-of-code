if __name__ == "__main__":
    l = sorted([int(i) for i in open("input.txt", "r").readlines()])
    l = [0] + l + [max(l) + 3]
    c = [1] + [0]*(len(l) - 1) 
   
    for i in range(1, len(l)):
        s = 0
        for j in range(i - 1, -1, -1):
            if l[i] - l[j] <= 3:
                s += c[j]
            else:
                break
        c[i] = s
    print(c[len(c) - 1])
