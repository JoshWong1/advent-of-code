
def findRow(s, low, high):
    if len(s) <= 1:
        if s == "F" or s == "L":
            return low
        else:
            return high
    mid = (high + low) // 2
    
    if s[0] == "F" or s[0] == "L":        
        return findRow(s[1:], low, mid)
    else:       
        return findRow(s[1:], mid + 1, high)
    
if __name__ == "__main__":
    result = 0
    l = open("input.txt", "r").readlines()
    ids = []
    
    for seat in l:        
        row = seat[0:7]
        col = seat[7:10]
        r = findRow(row, 0, 127)
        c = findRow(col, 0, 7)
        ide = r * 8 + c
        ids.append(ide)

    for i in range(0, 1028):
        a = i - 1
        b = i + 1
        if a in ids and b in ids and i not in ids:
            print(i)
            break
