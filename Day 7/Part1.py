def findAllColors(d, color, colors):
   if color not in d:
      return 0   
   total = 0
   for c in d[color]:
      if c not in colors:
         colors.append(c)
         total += 1 + findAllColors(d, c, colors)
   return total        

if __name__ == "__main__":
   l = open("input.txt", "r").readlines()    
   d = {}
   colors = []
   
   for line in l:
      items = line.split("bags contain")
      firstBag = items[0].strip()
      sub = []
      
      for i in items[1].split(", "):
         sub.append(i.strip()[1:].strip().split("bag")[0].strip())
         for color in sub:
            if color not in d:
               d[color] = []
            if firstBag not in d[color]:
               d[color].append(firstBag)
   
   n = findAllColors(d,'shiny gold', colors)
   print(n) 
