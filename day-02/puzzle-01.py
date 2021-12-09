with open('input.txt') as f:
    reader = map(lambda line: line.strip().split(), f.readlines())

hor, dep = 0, 0
for row in reader:
    direction, value = row[0], int(row[1])
    if direction == 'forward':
        hor += value
    elif direction == 'down':
        dep += value
    elif direction == 'up':
        dep -= value

print(hor * dep)

