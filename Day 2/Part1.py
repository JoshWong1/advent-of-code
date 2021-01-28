def isValid(low, high, letter, a):
    num = 0
    for c in a:
        if c == letter:
            num += 1
    if low <= num <= high:
        return True
    else:
        return False
    
if __name__ == "__main__":
    count = 0
    l = open("input.txt", "r").readlines()
    for line in l:
        items = line.split()
        nums = items[0].split("-")
        low = int(nums[0])
        high = int(nums[1])
        letter = items[1][0]
        a = items[2]
     
        if isValid(low, high, letter, a):
            count += 1
    print(count)
