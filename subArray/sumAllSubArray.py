def sum(A, s, e):
    sum = 0
    for i in range(s,e+1):
        sum = sum + A[i]
    print(sum)

def sumAllSubArray(A , n):
    for s in range(n):
        for e in range(s,n):
            sum(A, s, e)

    
A = [1, 2, 3]
n = len(A)
sumAllSubArray(A, n)

