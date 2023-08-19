def subArray(A , s , e):
    SA = []
    for i in range(s , e+1):
        SA.append(A[i])
    return SA

A = [2, 4, 6, 8, 10, 12]
n = len(A)
s = 2
e = 5
print(subArray(A , s , e))