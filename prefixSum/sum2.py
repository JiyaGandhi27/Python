def prefixSum(A ,n):
    PS = []
    PS.append (A[0])
    for i in range(1, n):
        PS.append(PS[i-1] + A[i])
    return PS
A = [1, 2, 3, 4, 8, 10]
n = len(A)
print(prefixSum(A,n))
def sum (A , n , PS):
    sl = 0
    sr = 0
    for i in range(n):
        sl = 0
        sr = 0
        if(i == 0):
            sl = 0
            sr = PS[n-1] - PS[0]
        elif(i == n-1):
            sl = PS[n-2]
            sr = 0
        else:
            sl = PS[i-1]
            sr = PS[n-1]-PS[i]
        if(sl == sr):
            return True  
    return False
A = [1, 2, 3, 4, 8, 10]
n = len(A)
PS = prefixSum(A,n)
print(sum(A , n , PS))