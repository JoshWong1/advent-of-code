if __name__ == "__main__":    
    groups = open("input.txt", "r").read().split("\n\n")    
    sol = 0
    
    for group in groups:
        found = set()
        for c in group:
            if c not in found and c != "\n":
                found.add(c)
                sol += 1
    print(sol)
