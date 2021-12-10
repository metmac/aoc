def marshall(data):
    rands = data[0].split(",")
    data = [list(map(int,x)) for x in [y.split() for y in [z for z in data[2:]]]]
    boards = [data[x:x+5] for x in range(len(data)) if x % 6 == 0]
    return {
        "rand": [int(a) for a in rands],
        "boards": [
            {
                "index": x,
                "rows": y,
                "cols": list(zip(*y))
            }
            for x,y in enumerate(boards)
        ]
    }

def winable(rand,board):
    board = board["rows"] + board["cols"]
    # return intersection against each row if len of the union is 5... i.e a win condition
    wins = [z for z in [set(rand) & set(x) for x in board] if len(z) == 5]
    if len(wins) == 0:
        return None
    return wins

def fastWinCondition(rand,wins):
    # get the earliest number index of any win condition
    # win_min_index = min([max(z) for z in map(lambda x:set(map(rand.index,x)),wins)])
    win_min = min(map(lambda x:set(map(rand.index,x)),wins) ,key=lambda x: max(x))
    return win_min

def unmark(rand,board,max_headroom):
    # Performs a set difference between a board's rows and the random set upto
    # the last winning condition index. Returns the sum of every number left on the board
    maxx = max(max_headroom)
    rand = rand[:maxx+1]
    board = board["rows"]
    # Didnt like this -> sum(sum([list(z) for z in [set(x) - set(rand) for x in board] if len(z) != 0],[]))
    return sum(sum([list(z) for z in [set(x) - set(rand) for x in board]],[]))


def win_result(data):
    rand = data["rand"]
    return [
            {
                "index": x["index"],
                "won_at": fastWinCondition(rand=rand, wins=winable(rand,x)),
                "unmarked_sum": unmark(rand=rand,board=x,max_headroom=fastWinCondition(rand=rand, wins=winable(rand,x))),
                "final_score": unmark(rand=rand,board=x,max_headroom=fastWinCondition(rand=rand, wins=winable(rand,x))) * rand[max(fastWinCondition(rand=rand, wins=winable(rand,x)))]
            }
            for x in data["boards"] if winable(rand,x) != None
        ]

def part1(winning):
    winning.sort(key= lambda x: max(x.get("won_at")))
    return winning

def part2(winning):
    winning.sort(reverse=True, key= lambda x: max(x.get("won_at")))
    return winning

if __name__ == "__main__":
    input = [x.strip() for x in open("./input.txt", "r")]
    data = marshall(input)
    wins = win_result(data)

    print(f"part1 answer is {part1(wins)[0]}")
    print(f"part2 answer is {part2(wins)[0]}")
