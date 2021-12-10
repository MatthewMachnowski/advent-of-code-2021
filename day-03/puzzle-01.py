with open('input.txt') as f:
    lines = f.read().split('\n')

balance = [0] * len(lines[0])

for line in lines:
    for count, bit in enumerate(line):
        if bit == '1':
            balance[count] += 1
        else:
            balance[count] -= 1

gamma, epsilon = "", ""

for bit in balance:
    if bit > 0:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

print(int(gamma, 2) * int(epsilon, 2))


