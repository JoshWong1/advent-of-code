import re
def isValid(tag, value):
    eyeColors = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
    if tag == 'byr':
        return 1920 <= int(value) <= 2002
    elif tag == 'iyr':
        return 2010 <= int(value) <= 2020
    elif tag == 'eyr':
        return 2020 <= int(value) <= 2030
    elif tag == 'hgt':
        val = int(value[:-2])
        typ = value[-2:]
        if typ == 'cm':
            return 150 <= val <= 193
        elif typ == 'in':
            return 59 <= val <= 76
    elif tag == 'ecl':
        return value in eyeColors
    elif tag == 'hcl':
        return re.match('^#[a-f0-9]{6}$', value)
    elif tag == 'pid':
        return re.match('^[0-9]{9}$', value)
    
if __name__ == "__main__":
    l = open("input.txt", "r").read().split("\n\n")
    
    valid = 0    
    for passport in l:
        tags = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
        for item in passport.split():
            tag = item[0:3]            
            if tag in tags:
                val = item[4:]  
                if not isValid(tag, val):
                    break               
                tags.remove(tag)
        if not tags:
            valid += 1
    print(valid)  
