import numpy as np


with open('input.txt') as f:
    data = [f.rstrip() for f in f.readlines()[2:]]


def get_bingo_input():
    with open('input.txt') as f:
        return list(map(lambda a: int(a), f.read().split("\n")[:1][0].split(',')))


def chunks(lst, size):
    for i in range(0, len(lst), size):
        yield lst[i:i + size]


def get_bingo_board(lst):
    lst = list(filter(lambda a: a != '', lst))
    lst = list(map(lambda a: [int(x) for x in a.split()], lst))
    return list(chunks(lst, 5))


boards = np.array(get_bingo_board(data))
found_board = False

for bingo_input in get_bingo_input():
    if found_board:
        break
    for board in boards:
        board[board == bingo_input] = 0
        if 0 in np.sum(board, axis=0) or 0 in np.sum(board, axis=1):
            print(np.sum(board) * bingo_input)
            found_board = True
