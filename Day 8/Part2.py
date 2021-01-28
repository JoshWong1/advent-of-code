import copy

def findCommand(commands, i, acc):
    while i < len(commands) - 1:       
        command = commands[i]
        command[2] += 1
        if command[2] > 1: return -1        
        p = process(command, i, acc)
        acc = p[1]
        i = p[0]
    return acc

def process(command, i, acc):
    if command[0] == "acc":
        acc += command[1]
        i+= 1
    elif command[0] == "jmp":
        i+= command[1]
    else:
        i+=1
    return (i, acc)
    
def swap(command):
    if command == "jmp":
        return "nop"
    else:
        return "jmp"
        
if __name__ == "__main__":
    l = open("input.txt", "r").readlines()
    commands = [[line[0:3], int(line[4:].strip()), 0] for line in l]
    acc = 0    
    i = 0
    
    while i < len(l) - 1:
        command = commands[i]
        if command[0] == "acc":
            acc += command[1]
            command[2] += 1
            i += 1
        else:
            command[0] = swap(command[0])  
            sol = findCommand(copy.deepcopy(commands), i, acc)
            if sol != -1:
                print(sol)
                break
            else:                
                command[0] = swap(command[0])
                command[2] += 1
                i = process(command, i, acc)[0]
