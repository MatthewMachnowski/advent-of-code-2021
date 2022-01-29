with open("input.txt") as f:
    data = [int(i) for i in f.read().strip().split(',')]

positions = [0] * max(data)
for crab_pos in data:
    for pos in range(len(positions)):
        side = abs(crab_pos - pos)
        positions[pos] += int((side + 1) * side / 2)
ans = min(positions)

print(ans)
