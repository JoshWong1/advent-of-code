def findAllColors(d, color, colors):
   if color not in d:
      return 0   
   total = 0
   for c in d[color]:
      if c not in colors:
         colors.add(c)
         total += 1 + findAllColors(d, c, colors)
   return total        

if __name__ == "__main__":
   l = open("input.txt", "r").readlines()
   
   d = {}     
   for line in l:
      firstBag, bags = line.split(" bags contain ")  
      for bag in bags.split(", "):
         color = bag[2:].split(" bag")[0]
         if color not in d:
            d[color] = {firstBag}
         else:
            d[color].add(firstBag)
    
   colors = set()
   n = findAllColors(d,'shiny gold', colors)
   print(n) 
