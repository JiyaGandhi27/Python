def prefixSum (A , n, i):
    sL = 0
    sR = 0
    for i in range(0 , i-1):
        sL += 1
    print(sL)
    


A = [1, 2, 3, 4, 8, 10]
n = len(A)
print(prefixSum(A , n , 3))