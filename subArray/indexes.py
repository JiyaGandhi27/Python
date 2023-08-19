def indexes(A):
    k = 10
    n = len(A)
    for i in range(n):
        for j in range(i + 1,n):
            if (A[i] + A[j] == k) and i!= j:
                return True
    return False
A = [1,2,3,0,-1,6,5]
print(indexes(A))


