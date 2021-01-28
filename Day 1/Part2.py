if __name__ == "__main__":
    f = open("input.txt", "r")
    l = f.readlines()
    for i in l:
        d = {}
        j = int(i)
        total = 2020 - j
        for item in l:
            item = int(item)
            if not(item in d):
                d[total - item] = 1
            else:
                x = (total - item) * item  * j
                print(x)
                break
