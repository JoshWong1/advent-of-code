def recursiveCombat(p1, p2):
    cache = set()
    while p1 and p2:          
        if (tuple(p1), tuple(p2)) in cache:
            return (1, p1, p2)        
        cache.add((tuple(p1), tuple(p2)))  
        
        card1, card2 = p1.pop(0), p2.pop(0)
    
        if card1 <= len(p1) and card2 <= len(p2):
            winner = recursiveCombat(p1[:card1], p2[:card2])[0]
        else:
            winner = 1 if card1 > card2 else 2

        if winner == 1:
            p1 += [card1, card2]
        else:
            p2 += [card2, card1]

    winner = 1 if p1 else 2
    return (winner, p1, p2)
        
    
if __name__ == "__main__":

    l = open("input.txt", "r").read().split("\n\n")
    
    ps = []
    for item in l:
        cards = item.split("\n")
        ps.append([int(cards[j]) for j in range(1, len(cards))])

    result = recursiveCombat(ps[0], ps[1])
    winDeck = result[result[0]]
   
    s = 0
    for i, card in enumerate(winDeck):
        s += card * (len(winDeck) - i)   
    print(s)
