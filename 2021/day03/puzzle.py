def part1(data):
    gamma,epsilon = [],[]
    for position in range(0,12):
        sig = [dlog[position] for dlog in data]
        t = [x for x in sig if x == "1"]
        f = [x for x in sig if x != "1"]
        if (len(t) > len(f)):
            gamma.append(1)
            epsilon.append(0)
        else:
            gamma.append(0)
            epsilon.append(1)
    gDec = int("".join(str(x) for x in gamma), 2)
    eDec = int("".join(str(x) for x in epsilon), 2)
    return gDec * eDec

def reduceSet(data,position,sig):
    if len(data) == 1:
        return data
    t = [x for x in data if x[position] == "1"]
    f = [x for x in data if x[position] == "0"]
    if sig == True:
        if len(t) < len(f):
            return f
        return t
    else:
        if len(t) < len(f):
            return t
        return f

def part2(data):
    o2,c02 = data,data
    for position in range(0,12):
        o2 = reduceSet(o2,position,True)
        c02 = reduceSet(c02,position,False)
    print (f"o2 = {int(o2[0],2)} co2 = {int(c02[0],2)}")
    return int(o2[0],2) * int(c02[0],2)

if __name__ == "__main__":
    data = [x for x in [x.strip() for x in open("./input.txt", "r")] ]
    print(f"part1 answer is {part1(data)}")
    print(f"part2 answer is {part2(data)}")
