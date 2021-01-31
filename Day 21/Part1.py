if __name__ == "__main__":
    with open("input.txt", "r") as f:
        l = [line.replace("contains", "").replace(")", "").strip() for line in f]

    l = [i.split(" ( ") for i in l]
    l = [[set(ingrs.split()), set(alrgs.split(", "))] for ingrs, alrgs in l]
 
    ingredients = set()
    for ingrs, _ in l:
        ingredients = ingredients.union(ingrs)
     
    d = {}
 
    for ingrs, alrgs in l:
        for alrg in alrgs:
            d[alrg] = d[alrg].intersection(ingrs) if alrg in d else ingrs    
    
    for item in d.values():
        ingredients = ingredients.difference(item)
  
    s = 0           
    for ingrs, _ in l:
        for i in ingrs:            
            s += i in ingredients
    print(s)
