if __name__ == "__main__":
    sol = 0
    groups = open("input.txt", "r").read().split("\n\n")

    for group in groups:        
        people = group.split()
        letters = [(people[0][i:i+1]) for i in range(0, len(people[0]))] 
        
        for person in people:            
            for letter in letters[:]:
                if letter not in person:
                    letters.remove(letter)
                    
        sol += len(letters)            
    print(sol)
