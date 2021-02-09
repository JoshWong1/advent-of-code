def findSum(l, s):
    d = {}
    for n in l:
        num = int(n)
        if int(n) in d:
            return True
        d[s - num] = 0
    return False

if __name__ == "__main__":
    nums = open("input.txt", "r").readlines() 
    
    for i in range(25, len(nums)):
        preamble = nums[i-25:i]
        if not(findSum(preamble, int(nums[i]))):
            print(nums[i])  
            break
