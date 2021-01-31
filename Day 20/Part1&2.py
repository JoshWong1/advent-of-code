import math
import copy

class Tile:
    def __init__(self, num, grid):
        self.num = num
        self.grid = grid
        self.update()
   
    def display(self):
        for item in self.grid:
            print(item)
    
    # Rotates tile 90 degrees clockwise
    def rotate(self):         
        self.grid = rotateGrid(self.grid)
        self.update()
       
    # Flips tile
    def flip(self):          
        self.grid = flipGrid(self.grid)
        self.update()
    
    # Updates left, right, bottom, and top edges of tile
    def update(self):
        self.top = list(self.grid[0])
        self.bottom = list(self.grid[-1])
        self.left = [s[0] for s in self.grid]
        self.right = [s[-1] for s in self.grid]
        
# Counts number of hash symbols in given grid
def count(l):
    total = 0
    for item in l:
        for s in item:
            if s == "#":
                total += 1
    return total

# Returns true if a sea monster exists at index i, j
def search(l, i, j):
    coords = [(i, j+18), (i+1, j), (i+1, j+5), (i+1, j+6), (i+1, j+11),\
           (i+1, j+12), (i+1, j+17), (i+1, j+18), (i+1, j+19), (i+2, j+1), \
           (i+2, j+4), (i+2, j+7), (i+2, j+10), (i+2, j+13), (i+2, j+16)]
    for x, y in coords:
        if l[x][y] != "#":
            return 0
    return 1

# Returns a new grid with its top, bottom, left, and right edges removed
def removeBorder(l):
    newL = []
    for i in range(1, len(l) - 1):
        newL.append(l[i][1:-1])
    return newL

# Rotates grid 90 degrees clockwise
def rotateGrid(l):
    newL = copy.deepcopy(l)    
    length = len(l)
    for i in range(length):
        s = ""
        for j in range(length):
            s += l[length - (j + 1)][i]
        newL[i] = s
    return newL

# Flips grid
def flipGrid(l):
    newL = copy.deepcopy(l)    
    length = len(l)
    for i in range(length):
        s = ""
        for j in range(length):
            s += l[length - 1 - i][j]
        newL[i] = s
    return newL    

# Given a grid of tiles, combines all tiles into a single grid
def joinTiles(arrangement):
    newL = []
    n = len(arrangement)
    for i in range(n):
        lengthTile = len(arrangement[i][0].grid[0])  
        for k in range(lengthTile):
            s = ""
            for j in range(n):            
                s += arrangement[i][j].grid[k]
            newL.append(s)
    return newL      
                      
# Finds first empty spot in grid to place a tile if it exists   
def findEmpty(l):
    for i in range(len(l)):
        for j in range(len(l[0])):
            if l[i][j] == 0:
                return(i, j)
    return None

# Returns true if tile can be placed in grid at index i, j
def isValid(l, i, j, tile):    
    if j > 0 and tile.left != l[i][j-1].right:
        return False
    elif i > 0 and tile.top != l[i-1][j].bottom:
        return False
    return True

def solve(tiles, l, k):
    
    # Look for empty spot in grid, if its full, we're done
    pos = findEmpty(l)    
    if not pos:
        return True
    row = pos[0]
    col = pos[1]  
    
    i = 0
    while i < len(tiles): 
        t = tiles[0]
        tiles.remove(t)
        
        # Try to place the tile in the grid by rotating and flipping it to see if it fits
        for j in range(8):
            if isValid(l, row, col, t): 
                """
                Try placing tile at the given position.  If this does not 
                lead to a solution, reset grid state and try another rotation 
                or tile
                """
                l[row][col] = t                

                if solve(tiles, l, k+1):
                    return True
                l[row][col] = 0                       
            
            t.rotate()
            if j == 3:          
                t.flip()                 
        tiles.append(t)       
        i+= 1
    return False
    
if __name__ == "__main__":

    # Parsing input
    l = open("input.txt", "r").read().split("\n\n")
    l = [tile.split("\n") for tile in l]

    # Creates list of tiles given input
    tiles = [Tile(int(tile[0].replace("Tile ", "").replace(":", "")), tile[1:]) for tile in l]
    
    # Initialize arrangement of tiles to a list of zeroes
    arrangement = []
    size = int(math.sqrt(len(tiles)))
    for i in range(size):
        arrangement.append([0 for j in range(size)])
    
    # Finds correct arrangement of tiles, Part 1 solution here    
    solve(tiles, arrangement, 0) 
    n = size - 1
    print("Part 1 answer: ", arrangement[0][0].num * arrangement[0][n].num * \
          arrangement[n][0].num * arrangement[n][n].num)    
       
    for item in arrangement:
        for tile in item:
            tile.grid = (removeBorder(tile.grid))
       
    # Create grid of all the tiles joined together      
    tilesCombined = joinTiles(arrangement)    
    cLength = len(tilesCombined)
    
    # Sea monster dimensions
    mLength = 20
    mHeight = 3         
    
    """
    Try each rotation of the grid to look for sea monsters. If found, break 
    loop, and calculate water roughness based on number of sea monsters found.
    """
    for x in range(8):
        n = 0
        for i in range(cLength - mHeight):
            for j in range(cLength - mLength):
                n += search(tilesCombined, i, j)
        if n>0:
            break        
        
        tilesCombined = rotateGrid(tilesCombined)
        if x == 3: tilesCombined = flipGrid(tilesCombined)
       
    # Part 2 solution
    print("Part 2 answer: ", count(tilesCombined) - 15 * n)
