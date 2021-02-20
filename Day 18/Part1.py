def applyOp(op, total, n):    
    return eval(str(total) + op + str(n)) if op else n

def solve(s, i):
    total = 0
    op = ""
    while i < len(s):        
        if s[i] in "+*":
            op = s[i]
        elif s[i] == "(":
            x, i= solve(s, i+1)
            total = applyOp(op, total, x)
        elif s[i] == ")":
            return total, i        
        else:
            total = applyOp(op, total, s[i])
        i += 1     
    return total, i
    
        
if __name__ == "__main__":
    with open("input.txt", "r") as f:
        l = [line.strip().replace(" ", "") for line in f]

    tol = 0
    for s in l:
        x = solve(s, 0)
        tol += x[0]
    print(tol)
