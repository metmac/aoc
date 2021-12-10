from collections import defaultdict
from typing import DefaultDict
import pprint as pp


def part1(fish_seed,days):
    tree_of_life = defaultdict(int)
    for y in range(0,9):
        tree_of_life[f"day0{y}"] = len([x for x in fish_seed if x == y])
    # for day in range(days):
    for y in range(0,9):
        if y != 0 and tree_of_life[f"day0{y}"] != 0:
            tree_of_life[f"day0{y}"] = tree_of_life[f"day0{y}"] - tree_of_life[f"day0{y}"]
            tree_of_life[f"day0{y+1}"] = tree_of_life[f"day0{y+1}"] + tree_of_life[f"day0{y}"]
        else:
            tree_of_life[f"day0{y}"] += tree_of_life[f"day0{y}"]
            tree_of_life[f"day0{y}"] += tree_of_life[f"day0{y}"]
            tree_of_life[f"day0{y}"] == 0


        pp.pprint(tree_of_life)
    print()
    return tree_of_life



def part2(data):
    pass


if __name__ == "__main__":
    data = [int(z) for x in open("./input.txt", "r") for z in x.strip().split(",")]

    print(f"part1 answer is {part1(data,19)}")
    print(f"part2 answer is {part2(data)}")
