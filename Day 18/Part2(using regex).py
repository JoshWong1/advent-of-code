import re
def solve(s):
    while "+" in s:
        r = re.search('(\d)*\+(\d)*', s).group()        
        s = s.replace(r, str(eval(r)), 1)
    return eval(s)

def solveP(s):
    while "(" in s or ")" in s:
        r = re.search('\([^(^)]*\)', s).group()
        s = s.replace(r, str(solve(r[1:-1])))
    return(solve(s))

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        l = [line.strip().replace(" ", "") for line in f]
    sol = 0
    for s in l:
        x = solveP(s)        
        sol += x
    print(sol)
