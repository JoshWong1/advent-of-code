if __name__ == "__main__":
   items = open("input.txt", "r").read().split("\n\n")

   #create list of other tickets
   ts = items[2].split("\n")[1:-1]
   tickets = []
   for s in ts:
      tickets.append([int(n) for n in s.split(',')])

   #create dict rules: key = rule name, value = list of min,max
   rules = {}
   for line in items[0].split("\n"):
      l = line.split(":")
      n1 = l[1].strip().split("or")[0].strip().split("-")
      n2 = l[1].strip().split("or")[1].strip().split("-")
      rules[l[0]] = [n1, n2]

   #find invalid tickets based on rules given
   invalid = []
   for ticket in tickets:
      for n in ticket:
         val = False
         for key in rules:
            if (n >= int(rules[key][0][0]) and n <= int(rules[key][0][1])) or (n <= int(rules[key][1][1]) and n >= int(rules[key][1][0])):
               val = True
               break
         if val == False:
            invalid.append(n)
          
   s = 0
   for n in invalid:
      s += n
   print(s) 
