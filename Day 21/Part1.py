if __name__ == "__main__":
    with open("input.txt", "r") as f:
        l = [line.replace("contains", "").replace(")", "").strip() for line in f]

    l = [i.split(" ( ") for i in l]
    l = [[set(item[0].split()), set(item[1].split(", "))] for item in l]
 
    ingredients = set()
    for item in l:
        ingredients = ingredients.union(item[0])
     
    d = {}
 
    for ings, algs in l:
        for alg in algs:
            d[alg] = d[alg].intersection(ings) if alg in d else ings    
    
    for item in d.values():
        ingredients = ingredients.difference(item)
  
    s = 0           
    for ings, _ in l:
        for i in ings:            
            s += i in ingredients
    print(s)
