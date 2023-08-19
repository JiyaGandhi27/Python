def prefixSum (A , n ):
    sl = 0
    sr = 0
    for i in range(n):
        sl = 0
        sr = 0
        for j in range(0 , i):
            sl = sl + A[j]

        for j in range(i+1 , n):
            sr = sr + A[j]
        
        if sl == sr:
            return True
    
    return False
A = [1, 2, 3, 4, 8, 10]
n = len(A)
print(prefixSum(A , n ))