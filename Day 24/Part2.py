import copy

if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        l = [line.strip() for line in f]
    
    d = {}
    c = {'e':[1, 0], 'w':[-1, 0,], 'ne': [0.5, 1], 'sw':[-0.5, -1], \
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
    
    n = 0
    while n < 100:
        white = {}
        black = {}
        for key in d:
            neighbours = [(key[0] + 1, key[1]), (key[0] - 1, key[1]), \
                          (key[0] + 0.5, key[1] - 1), (key[0] + 0.5, key[1] + 1),\
                          (key[0] - 0.5, key[1] + 1), (key[0] - 0.5, key[1] - 1)]
            
            for c in neighbours:
                if c not in d:
                    white[c] = white[c] + 1 if c in white else 1
                else:
                    black[c] = black[c] + 1 if c in black else 1              
                        
        b = copy.deepcopy(black)                
        for key in black: 
            if not (1 <= black[key] <= 2): b.pop(key)
        
        for key in white:
            if white[key] == 2: b[key] = 1        
        
        d = b
        n+=1  
        
    print(len(d))
