if __name__ == "__main__":
    with open("input.txt", "r") as f:
        l = [line.replace("contains", "").replace(")", "").strip() for line in f]

    l = [i.split(" ( ") for i in l]
    l = [[set(ingrs.split()), set(alrgs.split(", "))] for ingrs, alrgs in l]
     
    d = {} 
    for ingrs, alrgs in l:
        for alrg in alrgs:
            d[alrg] = d[alrg] & ingrs if alrg in d else ingrs    

    ls = [[key, d[key]] for key in d]    
    length = len(ls)
    
    for i in range(length):
        ls = sorted(ls, key=lambda t: len(t[1]))
        alrg, ingrs = ls.pop(0)
        ingr = ingrs.pop()
        d[alrg] = ingr
        for k in ls:
            k[1] = k[1] - {ingr}
        
    s = [d[key] for key in sorted(d.keys())]        
    print(','.join(s))
