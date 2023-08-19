A = [1, 1, 2, 2, 4, 4, 4, 8, 6, 2, 2, 4, 3]

frequency = {}

for key in A:
    if key in frequency:
        frequency[key] += 1
    else:
        frequency[key] = 1

print(frequency)
