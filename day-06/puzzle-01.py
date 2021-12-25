with open('input.txt') as f:
    data = f.read().strip().split(',')
    initial_state = [int(i) for i in data]

days = 80

for _ in range(days):
    n = len(initial_state)
    for i in range(n):
        if initial_state[i] == 0:
            initial_state[i] = 6
            initial_state.append(8)
        else:
            initial_state[i] -= 1

total = len(initial_state)
print(total)
