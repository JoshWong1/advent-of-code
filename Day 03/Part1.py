def countTrees(x, y, l):
    i, j, numTrees = 0, 0, 0
    length = len(l[0])
    while j <= len(l) - 2:
        i = (i + x) % (length)
        j += y
        if l[j][i] == '#':
            numTrees += 1
    return numTrees   

if __name__ == "__main__":
    l = [line.strip() for line in open("input.txt", "r")]
    print(countTrees(3, 1, l))
