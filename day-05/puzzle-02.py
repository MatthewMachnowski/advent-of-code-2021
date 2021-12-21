import numpy as np


with open("input.txt") as fin:
    data = fin.read().strip().split("\n")


def sign(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0


def parse_line(line):
    start, _, end = line.split(" ")
    start = [int(i) for i in start.split(",")]
    end = [int(i) for i in end.split(",")]
    direction = [sign(end[0] - start[0]), sign(end[1] - start[1])]
    return start, end, direction


lines = [parse_line(line) for line in data]

max_x = 0
max_y = 0
for li in lines:
    max_x = max(max_x, li[0][0], li[1][0])
    max_y = max(max_y, li[0][1], li[1][1])

cover = np.zeros((max_x + 1, max_y + 1))
for li in lines:
    start, end, direction = li
    p = start
    while p != end:
        cover[p[0], p[1]] += 1
        p[0] += direction[0]
        p[1] += direction[1]
    cover[end[0]][end[1]] += 1

ans = 0
for count in cover.flatten():
    ans += count >= 2

print(ans)
