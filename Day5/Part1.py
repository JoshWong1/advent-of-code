
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
    l = open("input.txt", "r").readlines()
    maxID = 0
    
    for seat in l:        
        row = seat[0:6]
        col = seat[7:10]
        r = findRow(row, 0, 127)
        c = findRow(col, 0, 7)
        ide = r * 8 + c
        maxID = max(maxID, ide)   
        
    print(maxID)
