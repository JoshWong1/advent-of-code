if __name__ == "__main__":
    with open("input.txt", "r") as f:
        l = [line.replace("contains", "").replace(")", "").strip() for line in f]

    l = [i.split(" ( ") for i in l]
    l = [[set(item[0].split()), set(item[1].split(", "))] for item in l]
     
    d = {}
 
    for ingrs, alrgs in l:
        for alrg in alrgs:
            d[alrg] = d[alrg].intersection(ingrs) if alrg in d else ingrs    

    ls = [[key, d[key]] for key in d]    
    length = len(ls)
    
    for i in range(length):
        ls = sorted(ls, key=lambda t: len(t[1]))
        alrg, ingrs = ls.pop(0)
        ingr = ingrs.pop()
        d[alrg] = ingr
        for k in ls:
            k[1] = k[1].difference(ingr)
    
    s = [d[key] for key in sorted(d.keys())]        
    print(','.join(s))
