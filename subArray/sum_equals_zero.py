def prefixSum(A, n):
    PS = []
    PS.append(A[0])
    for i in range(1, n):
        PS.append(PS[i-1] + A[i])
    return PS

def sum(A, n):
    PS = []
    PS = prefixSum(A,n)
    
    count = 0
    for s in range(n):
        sum = 0
        for e in range(s, n):
            if s == 0:
                sum = PS[e]
            else:
                sum = PS[e] - PS[s-1]

            if sum == 0:
                count += 1
           
    print(count)

A = [1, -1, -5, 5, -10, 7, 3, 2]
n = len(A)
sum(A, n)