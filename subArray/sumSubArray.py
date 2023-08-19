def subArray(A , s , e):
    SA = []
    sum = 0
    for i in range(s , e+1):
        sum = sum + A[i]
    return sum

A = [2, 4, 6, 8, 10, 12]
n = len(A)
s = 2
e = 5
print(subArray(A , s , e))