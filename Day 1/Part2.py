if __name__ == "__main__":
    l = open("input.txt", "r").readlines()
    for i in l:
        s = set()
        j = int(i)
        total = 2020 - j
        for num in l:
            n = int(num)
            if not(n in s):
                s.add(total - n)
            else:
                print((total - n) * n  * j)
                break
        else:
            continue
        break
