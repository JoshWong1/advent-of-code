if __name__ == "__main__":
    l = open("input.txt", "r").readlines()
    s = set()
    N = 2020
    for i in l:
        n = int(i)
        if n in s:
            break
        else:
            s.add(N - n)
