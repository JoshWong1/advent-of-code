def isValid(min, max, letter, a):
    num = 0
    for c in a:
        if c == letter:
            num += 1
    if num >= min and num <= max:
        return True
    else:
        return False
    
if __name__ == "__main__":
    count = 0
    l = open("input2.txt", "r").readlines()
    for line in l:
        items = line.split()
        nums = items[0].split("-")
        min = int(nums[0])
        max = int(nums[1])
        letter = items[1][0]
        a = items[2]
     
        if isValid(min, max, letter, a):
            count += 1
    print(count)
