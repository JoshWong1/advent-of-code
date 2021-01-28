def isValid(low, high, letter, a):
    if a[low - 1] == letter and a[high - 1] != letter:
        return True  
    elif a[high - 1] == letter and a[low - 1] != letter:   
        return True
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
