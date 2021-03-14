def rotate(angle, waypoint):
    n = angle//90
    for i in range(n):
        waypoint = [waypoint[1], -waypoint[0]]
    return waypoint

if __name__ == "__main__":
  
    l = [[line[0], int(line.strip()[1:])] for line in open("input.txt", "r")]
   
    dirs = {'N': [0,1], 'S': [0,-1], 'E': [1,0], 'W': [-1,0]}
    waypoint = [10, 1]
    coord = [0, 0]
    
    for d, val in l:
        if d in dirs:
            waypoint[0] += dirs[d][0] * val
            waypoint[1] += dirs[d][1] * val
        elif d == "L":
            waypoint = rotate(360 - val, waypoint)       
        elif d == "R":
            waypoint = rotate(val, waypoint)
        else: 
            coord[0] += waypoint[0] * val
            coord[1] += waypoint[1] * val
            
    print(abs(coord[0]) + abs(coord[1]))
