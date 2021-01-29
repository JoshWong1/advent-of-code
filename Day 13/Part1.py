if __name__ == "__main__":
    with open("input.txt", "r") as f:
        l = [line.strip() for line in f]
    timestamp = int(l[0])
    buses = [int(a.strip()) for a in l[1].split(",") if a != "x"]

    nextTime = []
    
    for bus in buses:
        time = 0
        while time <= timestamp:
            time += bus
        nextTime.append((time, bus))
    print(min(nextTime), (min(nextTime)[0] - timestamp) * min(nextTime)[1])
