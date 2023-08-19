def printSubArray(A, s, e):
    for i in range(s, e+1):
        print(A[i], end = " ")
    print()

def printAllSubArray(A , n):
    for s in range(n):
        for e in range(n):
            printSubArray(A, s, e)
A = [1, 2, 3]
n = len(A)
printAllSubArray(A, n)