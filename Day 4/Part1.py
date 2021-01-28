if __name__ == "__main__":
    l = open("input.txt", "r").read().split("\n\n")    
    valid = 0    
    for passport in l:
        tags = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
        items = passport.split()
        for item in items:
            tag = item[0:3]            
            if tag in tags:            
                tags.remove(tag)
        if not tags:
            valid += 1
    print(valid)  
