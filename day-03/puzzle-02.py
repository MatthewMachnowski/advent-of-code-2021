with open('input.txt') as f:
    lines = f.read().split('\n')


def bits_balance(numbers, index):
    balance = 0
    for line in numbers:
        if line[index] == '1':
            balance += 1
        else:
            balance -= 1
    return balance


def filter_binary_numbers(bit, index, numbers):
    return list(filter(lambda number: number[index] == bit, numbers))


def generator_rating(numbers, rating_values):
    lst = numbers
    index = 0
    while len(lst) > 1:
        balance = bits_balance(lst, index)
        rating = rating_values[0] if balance >= 0 else rating_values[1]
        lst = filter_binary_numbers(rating, index, lst)
        index += 1
    return lst[0]


oxygen = int(generator_rating(lines, ("1", "0")), 2)
co2 = int(generator_rating(lines, ("0", "1")), 2)

print(oxygen * co2)
