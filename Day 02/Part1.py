def isValid(low, high, letter, s):
    num = 0
    for c in s:
        if c == letter: num += 1
        
    return low <= num <= high
    
if __name__ == "__main__": 
    l = [line.split() for line in open("input.txt", "r").readlines()]
    count = 0
    for r, c, s in l:       
        low, high = r.split("-")     
        count += isValid(int(low), int(high), c[0], s)
    print(count)
