def findNumBags(d, color):
   if color not in d:
      return 0   
   total = 0
   for c in d[color]:
      total += c[1] + findNumBags(d, c[0]) * c[1]
   return total     
        

if __name__ == "__main__":
   l = open("input.txt", "r").readlines()    
   d = {}
   
   for line in l:
      firstBag, bags = line.split(" bags contain ")
      d[firstBag] = [(bag[2:].split(" bag")[0], int(bag[0])) for bag in bags.split(", ") if not bag[0] == 'n']

   n = findNumBags(d,'shiny gold')
   print(n)
