if __name__ == "__main__":
    sol = 0
    groups = open("input.txt", "r").read().split("\n\n")
    for group in groups:
        found = []
        for c in group:
            if c not in found and c != "\n":
                found.append(c)
                sol += 1
    print(sol)
