import copy

def valid(n, low1, high1, low2, high2):
   return low1 <= n <= high1 or low2 <= n <= high2

if __name__ == "__main__":
   items = open("input.txt", "r").read().split("\n\n")      
   
   #my ticket   
   myseat = items[1].split("\n")[1].strip().split(",")

   #create list of other tickets
   ts = items[2].split("\n")[1:]
   tickets = [[int(n) for n in s.split(",")] for s in ts]

   #create dict rules: key = rule name, value = list of min,max
   rules = {}
   for line in items[0].split("\n"):
      l = line.split(":")
      n1 = l[1].strip().split("or")[0].strip().split("-")
      n2 = l[1].strip().split("or")[1].strip().split("-")
      rules[l[0]] = [n1, n2]

   #find invalid tickets and remove them from list of tickets
   invalid = []
   for ticket in tickets:  
      for n in ticket:  
         for key in rules:
            if valid(n, int(rules[key][0][0]), int(rules[key][0][1]), int(rules[key][1][0]), int(rules[key][1][1])):
               break
         else:
            invalid.append(ticket)
            break
            
   for item in invalid:
      tickets.remove(item)
  
   #find all possible rule, index assignments 
   order = []
   for i in range(len(tickets[0])):
      order.append([])
      for key in rules:  
         for t in tickets:
            n = t[i]
            if not valid(n, int(rules[key][0][0]), int(rules[key][0][1]), int(rules[key][1][0]), int(rules[key][1][1])):          
               break
         else:            
            order[i].append(key)
             
   order2 = copy.deepcopy(order)
   order2.sort(key=len)

   #given list of all possible (rule, index) assignments, 
   #start from list of size 1 and work up to find correct assignments
   d2 = {}
   for i in range(0, 20):
      for j, item in enumerate(order):
         if item == order2[i]:
            for item2 in item:
               if item2 not in d2:
                  d2[item2] = j
                  break
  
   #find all values in my seat with departure in key name 
   #multiply them together to find solution
   s = 1
   for key in d2:
      if "departure" in key:
         s *= int(myseat[d2[key]])
   print(s)
