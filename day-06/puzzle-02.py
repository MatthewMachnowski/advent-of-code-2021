from collections import defaultdict


with open('input.txt') as f:
    data = f.read().strip().split(',')
    initial_state = defaultdict(int)
    for i in data:
        initial_state[int(i)] += 1

days = 256

for _ in range(days):
    new_age = defaultdict(int)
    for age in initial_state:
        if age == 0:
            new_age[6] += initial_state[age]
            new_age[8] = initial_state[age]
        else:
            new_age[age - 1] += initial_state[age]

    initial_state = new_age

total = 0
for key in initial_state:
    total += initial_state[key]
print(total)
