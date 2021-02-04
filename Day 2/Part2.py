def isValid(low, high, letter, a):
    return (a[low - 1] == letter and a[high - 1] != letter) or \
           a[high - 1] == letter and a[low - 1] != letter

if __name__ == "__main__":
    l = [line.split() for line in open("input.txt", "r").readlines()]  
    
    count = 0
    for r, c, s in l:       
        low, high = r.split("-")    
        if isValid(int(low), int(high), c[0], s): count += 1
           
    print(count)
