if __name__ == "__main__":
    
    l = [[line[0], int(line.strip()[1:])] for line in open("input.txt", "r")]
    
    dirs = {'N': [0,1], 'S': [0,-1], 'E': [1,0], 'W': [-1,0]}
    direction = 0
    coord = [0,0]
    
    for d, num in l:
        if d in dirs:
            coord[0] += dirs[d][0] * num
            coord[1] += dirs[d][1] * num
        elif d == "L":
            direction = (direction + 360 - num) % 360
        elif d == "R":
            direction = (direction + num) % 360
        else:
            if direction == 0:
                coord[0] += num
            elif direction == 270:
                coord[1] += num
            elif direction == 180:
                coord[0] -= num
            elif direction == 90:
                coord[1] -= num                
    
    print(abs(coord[0]) + abs(coord[1]))            
