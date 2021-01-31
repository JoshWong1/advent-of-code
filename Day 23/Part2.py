import time
class Node:
    def __init__(self, data):
        self.val = data
        self.next = None     
        
def nextDest(curr, temp, low, high):
    dest = curr        
    while True:  
        dest = dest - 1 if dest > low else high
        if dest not in temp: return dest
            
if __name__ == "__main__":
    start = time.time()
    l = list(open("input.txt", "r").read())
    l = [int(n) for n in l]           
    Nodes = {}
    N = 1000000
    
    for i in range(1, N + 1):
        Nodes[i] = Node(i)         
    
    for i in range(0, len(l)):
        if i != len(l) - 1:
            Nodes[l[i]].next = Nodes[l[i+1]]
        else:
            Nodes[l[i]].next = Nodes[len(l) + 1]
    
    for i in range(10, N + 1):
        if i < N:
            Nodes[i].next = Nodes[i+1]
        else:
            Nodes[i].next = Nodes[l[0]]
    
    currentNode = Nodes[l[0]]
    high = N
    low = min(l)  
    
    for i in range(10 * N):
        removeNodeStart = currentNode.next
        removeNodeEnd = currentNode.next.next.next
        
        currentNode.next = removeNodeEnd.next
        
        temp = [removeNodeStart.val, removeNodeStart.next.val, removeNodeEnd.val]        
        dest = nextDest(currentNode.val, temp, low, high)
        
        j = Nodes[dest]
        removeNodeEnd.next = j.next
        j.next = removeNodeStart
        currentNode = currentNode.next      
     
    print(Nodes[1].next.val * Nodes[1].next.next.val)
    print(time.time() - start)
