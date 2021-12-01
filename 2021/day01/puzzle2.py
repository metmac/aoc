a = [int(x.strip()) for x in open("./input.txt", "r") ]
b = [sum(a[x:x+3]) for x in range(len(a))]
c = len([x for x,y in enumerate(b) if y > b[x -1]])
