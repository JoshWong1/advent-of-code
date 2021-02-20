def applyOp(op, total, n):
    return eval(str(total) + op + str(n)) if op else n
  
def solve(s, i):
    total = 0
    op = ""
    while i < len(s):        
        if s[i] in "+*":
            op = s[i]
        elif s[i] == "(":
            x, i = solve(s, i+1)
            total = applyOp(op, total, x)
        elif s[i] == ")":
            return total, i        
        else:
            total = applyOp(op, total, s[i])
        i += 1     
    return total, i

def findIndex(s, a, b, i, incr):
    brackets = 0
    while True:
        if s[i] == a:
            brackets += 1
        elif s[i] == b:
            brackets -= 1
            if brackets == 0:
                return i
        elif s[i] != "*" and s[i] != "+":
            if brackets == 0:
                return i
        i += incr

def addBrackets(s):
    i = 0
    while i < len(s):
        if s[i] == "+":
            j = findIndex(s, ")", "(", i - 1, -1)          
            s = s[:j] + "(" + s[j:]            
            k = findIndex(s, "(", ")", i + 2, 1)
            s = s[:k+1] + ")" + s[k+1:]
            i += 1
        i += 1
    return s
    
        
if __name__ == "__main__":
    with open("input.txt", "r") as f:
        l = [line.strip().replace(" ", "") for line in f]  
        
    tol = 0
    for s in l:
        x, _ = solve(addBrackets(s), 0)
        tol += x
    print(tol)
