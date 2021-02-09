def findSet(l, target):
    for j in range(2, len(l)):
        queue = l[0:j]
        tol = sum(queue)
        for i in range(j, len(l)):
            tol -= queue.pop(0)
            tol += l[i]
            queue.append(l[i])
            if tol == target: return queue
    
if __name__ == "__main__":    
    nums = [int(n) for n in open("input.txt", "r").readlines()]
    target = 144381670
    ans = findSet(nums, target)
    print(min(ans) + max(ans)) 
