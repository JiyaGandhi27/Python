def prefixSum(A ,n):
    PS = []
    PS.append (A[0])
    for i in range(1, n):
        PS.append(PS[i-1] + A[i])
    return PS
A = [-3, 6, 2, 4, 5, 2, 8, -9, 3, 1]
n = len(A)
print(prefixSum(A,n))