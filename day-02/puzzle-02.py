with open('input.txt') as f:
    reader = map(lambda line: line.strip().split(), f.readlines())

hor, dep, aim = 0, 0, 0
for row in reader:
    direction, value = row[0], int(row[1])
    if direction == 'down':
        aim += value
    elif direction == 'up':
        aim -= value
    elif direction == 'forward':
        hor += value
        dep += value * aim

print(hor * dep)
