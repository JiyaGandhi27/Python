def sum(A):
    sum = 0
    for i in range(1, 4):
        sum += A[i]
    return sum
A = [-3, 6, 2, 4, 5, 2, 8, -9, 3, 1]
print(sum(A))
