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
      items = line.split("bags contain")
      firstBag = items[0].strip()
      sub = []
      for i in items[1].split(", "):
         if not(i.strip()[0] == 'n'):            
            sub.append((i[2:].strip().split(" bag")[0], int(i.strip()[0])))       
      d[firstBag] = sub
 
   n = findNumBags(d,'shiny gold')
   print(n)
