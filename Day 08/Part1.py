if __name__ == "__main__":
    l = open("input.txt", "r").readlines()
    commands = [[line[0:3], int(line[4:].strip()), 0] for line in l]
    acc = 0
    c = 0
    
    while c < len(l) - 1:
        command = commands[c]
        command[2] += 1
        if commands[2] > 1:
            print(acc)
            break
        if command[0] == "acc":
            acc += command[1]
            c += 1
        elif command[0] == "jmp":
            c += command[1]
        elif command[0] == "nop":
            c += 1
