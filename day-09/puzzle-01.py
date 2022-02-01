with open("input.txt") as f:
    lines = f.read().strip().split("\n")
    data = [[int(i) for i in list(line)] for line in lines]

ans = 0
for row in range(len(data)):
    for col in range(len(data[0])):
        low = True
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        for d in directions:
            rr = row + d[0]
            cc = col + d[1]

            if not ((0 <= rr < len(data)) and (0 <= cc < len(data[0]))):
                continue

            if data[rr][cc] <= data[row][col]:
                low = False
                break

        if low:
            ans += data[row][col] + 1

print(ans)
