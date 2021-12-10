# def marshall(data):
#     return [ {"cipher": data[x], "key": None, "output": data[x+1], "result": []} for x in range(len(data)) if x % 2 == 0 ]

def part1(data):
    for foo in data:
        for bar,baz in enumerate(foo):
            if foo.pop()


def part2(data):
    pass


if __name__ == "__main__":
    # data1 = [a for a in [z.split() for x in open("./input.txt", "r") for z in x.strip().split("|")][1::2]]
    # input = [x for x in open("./input.txt", "r") for z in x.strip().split("|")]
    data = [list(x.strip()) for x in open("./input.txt", "r")]
    answer1 = part1(data)
    answer2 = part2(data)
    print(f"part1 answer is {answer1}")
    print(f"part2 answer is {answer2}")
