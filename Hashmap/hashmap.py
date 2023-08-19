def pairs(A, n):
    k = 5
    pair = {}
    for i in range(0, n):
            diff = k - A[i]
            if diff in pair:
                return 1
            else:
                pair[A[i]] = i
    return 0
A = [1, 2, 3, 4]
n = len(A)
print(pairs(A, n))