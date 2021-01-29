if __name__ == "__main__":
    with open("input.txt", "r") as f:
        l = [line.strip() for line in f]

    buses = [(i, int(a.strip())) for i, a in enumerate(l[1].split(",")) if a != "x"]

    time = 0
    incr = buses[0][1]
    n = 1

    while True:
        time += incr
        if (time + buses[n][0]) % buses[n][1] == 0:
            incr = incr * buses[n][1]
            n += 1
            if n == len(buses):
                print(time)
                break
