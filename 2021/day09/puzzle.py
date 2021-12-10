def marshall(data):
    return [ {"cipher": data[x], "key": None, "output": data[x+1], "result": []} for x in range(len(data)) if x % 2 == 0 ]

def part1(data):
    output = [x["output"] for x in data]
    const_seg_map =  {2:1,3:7,4:4,7:8}
    for signal in data:
        signal["key"] = {const_seg_map[len(x)]: set(x) for x in signal["cipher"] if len(x) in [2,3,4,7]}
    return len([x for x in map(len,sum(output,[])) if x in [2,3,4,7]])

def part2(data):
    for signal in data:
        signal["key"].update( {
            9: next(set(x) for x in signal["cipher"] if len(x) == 6 and set(x).issuperset(signal["key"][4])),
            6: next(set(x) for x in signal["cipher"] if len(x) == 6 and not set(x).issuperset(signal["key"][1])),
            0: next(set(x) for x in signal["cipher"] if len(x) == 6 and set(x).issuperset(signal["key"][1]) and not set(x).issuperset(signal["key"][4])),
            3: next(set(x) for x in signal["cipher"] if len(x) == 5 and set(x).issuperset(signal["key"][1])),
            })
        signal["key"].update( {
            5: next(set(x) for x in signal["cipher"] if len(x) == 5 and set(x).issubset(signal["key"][6])),
            2: next(set(x) for x in signal["cipher"] if len(x) == 5 and not set(x).issubset(signal["key"][6]) and not set(x).issubset(signal["key"][3])),
        })
        signal["key_invert"] = {"".join(sorted(value)) : key for key,value in signal["key"].items()}
        signal["decode"] = [signal["key_invert"]["".join(sorted(x))] for x in signal["output"]]
        signal["result"] = int(''.join(map(str,signal["decode"])))
    return sum([x["result"] for x in data])


if __name__ == "__main__":
    # data1 = [a for a in [z.split() for x in open("./input.txt", "r") for z in x.strip().split("|")][1::2]]
    input = [z.split() for x in open("./input.txt", "r") for z in x.strip().split("|")]
    data = marshall(input)
    answer1 = part1(data)
    answer2 = part2(data)
    print(f"part1 answer is {answer1}")
    print(f"part2 answer is {answer2}")


# Napkin Math
# signal = [x["cipher"] for x in data]
# partial_cipher = [[(x,const_seg_map[len(x)]) for x in y if len(x) in [2,3,4,7]] for y in signal]
    # 1 = known len(2)
    # 4 = known len(4)
    # 7 = known len(3)
    # 8 = known len(7)
    # 9 = for len(6) and x.issuperset(4)
    # 6 = for len(6) and not x.issuperset(1)
    # 0 = not 6 or 9
    # 5 = x.issubset(6)
    # 2 = not x.issubset(6)
    # 3 = for len(5) if x.issuperset(1)

        # 9 = for len(6) and set(4) & set(7) this was wrong... for some reason.
