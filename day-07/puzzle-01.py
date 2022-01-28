with open("input.txt") as f:
    raw_data = f.read().strip().split(',')

data = [int(i) for i in raw_data]

max_pos = max(data)

