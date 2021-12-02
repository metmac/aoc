def part1(data):
    fwd = sum([int(x["val"]) for x in data if x["op"] == "forward"])
    up = sum([int(x["val"]) for x in data if x["op"] == "up"])
    down = sum([int(x["val"]) for x in data if x["op"] == "down"])
    print((down - up) * fwd)

def part2(data):
    hoz = dep =  aim = 0
    for move in data:
        if move["op"] == "forward":
            hoz +=  int(move["val"])
            dep += ( int(move["val"]) * aim)
        elif move["op"] == "up":
            aim -=  int(move["val"])
        elif move["op"] == "down":
            aim +=  int(move["val"])
    print(hoz * dep)

a = [ {"op": x[0],"val": x[1] } for x in [x.strip().split(" ") for x in open("./input.txt", "r")] ]
part1(a)
part2(a)
