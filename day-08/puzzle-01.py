with open("input.txt") as f:
    raw_data = f.read().split("\n")
    data = [line[line.index("|") + 2:].split(" ") for line in raw_data]

ans = 0
for output in data:
    for digit in output:
        if len(digit) in [2, 4, 3, 7]:
            ans += 1

print(ans)
