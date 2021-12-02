def part1():
    a = [ {"op": x[0],"val": x[1] } for x in [x.strip().split(" ") for x in open("./input.txt", "r")] ]
    fwd = sum([int(x["val"]) for x in a if x["op"] == "forward"])
    up = sum([int(x["val"]) for x in a if x["op"] == "up"])
    down = sum([int(x["val"]) for x in a if x["op"] == "down"])
    print((down - up) * fwd)

def part2():
    a = [ {"op": x[0],"val": x[1] } for x in [x.strip().split(" ") for x in open("./input.txt", "r")] ]
    hoz = dep =  aim = 0
    for move in a:
        if move["op"] == "forward":
            hoz +=  int(move["val"])
            dep += ( int(move["val"]) * aim)
        elif move["op"] == "up":
            aim -=  int(move["val"])
        elif move["op"] == "down":
            aim +=  int(move["val"])
    print(hoz * dep)
