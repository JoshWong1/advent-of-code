def findRow(s, low, high):
    if len(s) <= 1:
        if s == "F" or s == "L":
            return low      
        return high
    mid = (high + low) // 2
    if s[0] == "F" or s[0] == "L":
        return findRow(s[1:], low, mid)    
    return findRow(s[1:], mid + 1, high)
    
if __name__ == "__main__":
    l = open("input.txt", "r").readlines()
    
    maxID = 0
    for seat in l:        
        row, col = findRow(seat[0:7], 0, 127), findRow(seat[7:10], 0, 7)
        ide = row * 8 + col
        maxID = max(maxID, ide)   
        
    print(maxID)
