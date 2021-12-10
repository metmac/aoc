len([z for y,z in enumerate([int(x.strip()) for x in open("./input.txt", "r")])if z > [int(x.strip()) for x in open("./input.txt", "r")][y - 1]])
