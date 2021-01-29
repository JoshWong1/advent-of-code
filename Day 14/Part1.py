def pad(n, length):
    zeroes = ""
    for i in range(length):
        zeroes += "0"
    return zeroes + n

def applyMask(n, mask):
    n = str(n)[2:]
    s = pad(n, len(mask) - len(n))
    for i in range(len(mask)):
        if mask[i] == "0":
            s = s[0:i] + "0" + s[i+1:]
        elif mask[i] == "1":
            s = s[0:i] + "1" + s[i+1:]
    return s
    
if __name__ == "__main__":
    l = open("input.txt", "r").readlines()
    d={}
    mask = ""
    length = 0
    m = {}
    for line in l:
        if line[1] == "a":
            mask =  line.split("=")[1].strip()
            length = len(mask)
            d[mask] = []
        else:
            i = line.replace("mem", "").replace("[", "").replace("]", "").split("=")            
            d[mask].append([int(i[0].strip()), int(i[1].strip())])
            
    for mask in d:
        for item in d[mask]:
            mem = item[0]
            b = bin(item[1])
            new = int(applyMask(b, mask), 2)
            m[mem] = new

    print(sum(m.values()))
