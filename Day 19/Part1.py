import re
        
def buildReg(rules, value):
    reg = ""
    if value[0] == '"':
        reg = value[1]
    elif re.search('\|', value):
        options = value.split(' | ')
        reg = "(" + buildReg(rules, options[0]) + "|" + buildReg(rules, options[1]) + ")"
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

    reg = '^' + buildReg(d, d['0']) + '$'

    tol = 0
    for msg in msgs:
        if re.search(reg, msg):
            tol += 1
    print(tol)
