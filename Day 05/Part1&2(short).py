if __name__ == "__main__":
    l = [int(line.replace('B', '1').replace('F', '0').replace('L', '0').replace('R', '1'), 2) for line in open("input.txt", "r").readlines()]
    print("Part 1 answer:", max(l))
    print("Part 2 answer:", [i for i in range(min(l), max(l)) if not i in l][0])
