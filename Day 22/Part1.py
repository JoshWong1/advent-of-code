if __name__ == "__main__":
    l = open("input.txt", "r").read().split("\n\n")
    
    ps = []
    for item in l:
        cards = item.split("\n")
        ps.append([int(cards[j]) for j in range(1, len(cards))])
    
    p1 = ps[0]
    p2 = ps[1]

    while p1 and p2:
        card1 = p1.pop(0)
        card2 = p2.pop(0)
        if card1 > card2:
            p1 += [card1, card2]
        else:
            p2 += [card2, card1]

        if not p1 or not p2:
            break
    s = 0
    winner = p2 if p2 else p1
        
    for i, card in enumerate(winner):
        s += card * (len(winner) - i)   
    print(s)
