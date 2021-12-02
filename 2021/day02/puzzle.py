def part1(data):
    fwd = sum([x["val"] for x in data if x["op"] == "forward"])
    up = sum([x["val"] for x in data if x["op"] == "up"])
    down = sum([x["val"] for x in data if x["op"] == "down"])
    print((down - up) * fwd)

def part2(data):
    hoz,dep,aim = 0,0,0
    for move in data:
        if move["op"] == "forward":
            hoz += move["val"]
            dep += move["val"] * aim
        elif move["op"] == "up":
            aim -= move["val"]
        elif move["op"] == "down":
            aim += move["val"]
    print(hoz * dep)

if __name__ == "__main__":
    a = [ {"op": x[0],"val": int(x[1]) } for x in [x.strip().split(" ") for x in open("./input.txt", "r")] ]
    part1(a)
    part2(a)
