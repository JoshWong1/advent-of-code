def countTrees(x, y, l):
    i = 0
    j = 0
    numTrees = 0
    while j <= len(l) - 2:
        i = (i + x) % (len(l[j]))
        j += y
        if l[j][i] == '#':
            numTrees += 1
    return numTrees   

if __name__ == "__main__":
    l = [line.strip() for line in open("input3.txt", "r")]
    print(countTrees(3, 1, l))
