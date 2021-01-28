def findSet(l, target):
    j = 0
    while j < len(l):
        total = 0
        for i in range(j, len(l)):
            total += int(l[i])
            if total == target:
                return l[j:i+1]
            elif total > target:
                break       
        j += 1
    
if __name__ == "__main__":
    target = 144381670
    nums = open("input.txt", "r").readlines()
    ans = [int[n] for n in findSet(nums, target)]
    print(min(ans) + max(ans))
