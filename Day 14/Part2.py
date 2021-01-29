def pad(n, length):
    zeroes = ""
    for i in range(length):
        zeroes += "0"
    return zeroes + n

def applyMask(n, mask):
    n = str(n)[2:]
    nums = [pad(n, len(mask) - len(n))]
   
    for i in range(len(mask)):
        if mask[i] == "1":
            for j in range(len(nums)):
                nums[j] = nums[j][0:i] + "1" + nums[j][i+1:]
        elif mask[i] == "X":
            for j in range(len(nums)):
                s3 = nums[j][0:i] + "0" + nums[j][i+1:]
                nums[j] = nums[j][0:i] + "1" + nums[j][i+1:]                
                nums.append(s3)
    return nums    
    
if __name__ == "__main__":

    l = open("input.txt", "r").readlines()
    d = {}
    m = {}
    
    for line in l:
        if line[1] == "a":
            mask =  line.split("=")[1].strip()
            length = len(mask)
            d[mask] = []
        else:
            i = line.replace("mem", "").replace("[", "").replace("]", "").split("=")            
            d[mask].append([int(i[0].strip()), int(i[1].strip())])
   
        
    for mask in d:
        for mem, b in d[mask]:
            mem = bin(mem)
            memList = applyMask(mem, mask)
            for n in memList:
                m[int(n, 2)] = b

    print(sum(m.values()))
