if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        l = [line.strip() for line in f]
    
    d = {}
    c = {'e':[1, 0, 0], 'w':[-1, 0,], 'ne': [0.5, 1], 'sw':[-0.5, -1], \
         'nw':[-0.5, 1], 'se':[0.5, -1]}
    for line in l:
        coord = (0, 0)
        i = 0        
        while i < len(line):
            if line[i] in 'ew':
                coord = tuple(j + k for j, k in zip(coord, c[line[i]]))
                i+=1
            else:
                coord = tuple(j + k for j, k in zip(coord, c[line[i:i+2]]))
                i+=2
                
        if not coord in d:
            d[coord] = 1
        else:
            d.pop(coord)

    print(len(d))
