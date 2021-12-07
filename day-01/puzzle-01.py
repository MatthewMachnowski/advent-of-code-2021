with open('input.txt') as f:
    reader = f.read().split('\n')
    integer = [int(row) for row in reader]

increases = 0
for i in range(1, len(integer)):
    if integer[i] > integer[i - 1]:
        increases += 1

print(increases)
