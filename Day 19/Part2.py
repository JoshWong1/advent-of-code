import re
        
def buildReg(rules, value,):
    reg = "" 
    if value[0] == '"':
        reg = value[1]
    elif re.search('\|', value):
        options = value.split(' | ')
        reg = "("+ buildReg(rules, options[0]) + "|" + buildReg(rules, options[1])+")"
    else:
        options = value.split()
        for o in options:
            reg += buildReg(rules, rules[o])
    return reg

if __name__ == "__main__":
    l, m = open("input.txt", "r").read().split("\n\n")
    msgs = m.split()
    
    d = {}    
    for line in l.split("\n"):
        key, rules = line.split(":")
        d[key] = rules.strip()
        
    d['8'] = '42 | 42 8'
    d['11'] = '42 31 | 42 11 31' 

    reg42 = buildReg(d, d['42']) 
    reg31 = buildReg(d, d['31'])
    reg = '^(' + reg42 + ')+(' + reg31 + ')+$'

    tol = 0
    for msg in msgs:
        if len(msg) % 8 == 0 and re.search(reg, msg):
            length = int(len(msg)/8)
            ms = [msg[i*8:i*8+8] for i in range(length)]
            s = 0
            for item in reversed(ms):
                if re.search(reg31, item):
                    s += 1
                else:
                    break                
            tol += s < length/2
                
    print(tol)
