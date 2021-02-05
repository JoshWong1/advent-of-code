def valid(s):
    return 'byr:' in s and 'iyr:' in s and 'eyr:' in s and 'hgt:' in s and \
           'hcl:' in s and 'ecl:' in s and 'pid:' in s

if __name__ == "__main__":
    l = open("input.txt", "r").read().split("\n\n")    
    sol = 0    
    for passport in l:
        sol += valid(passport)    
    print(sol)  
