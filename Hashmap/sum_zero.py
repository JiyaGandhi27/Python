def prefixSum(A, n):
    PS = []
    PS.append(A[0])
    for i in range(1, n):
        PS.append(PS[i-1] + A[i])
    return PS

def sum_zero(A, n):
    PS = []
    PS = prefixSum(A, n)
    elements = set()
    count = 0

    print(PS)
 
    for i in range(n):
        num = PS[i]

        if(PS[i] == 0):
            count += 1
        if num in elements:
            count += 1     
        else:
            elements.add(PS[i])
    print(count)

A = [-1, 1, 2]
n = len(A)
sum_zero(A, n)