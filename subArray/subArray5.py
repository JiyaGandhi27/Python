def sum(A, n):
    for s in range(n):
        sum = 0
        for e in range(s, n):
            sum = sum + A[e]
            print(sum)
A = [1, 2, 3]
n = len(A)
sum(A, n)


