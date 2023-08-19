def countElements(A):
    n = len(A)
    count = 0
    maxNumber = max(A)
    for i in range(n):
        if A[i] == maxNumber:
            count = count + 1
    elements = n - count
    return elements
A = [1,3,-2,8,0,5,7,2,4,8,7]
print(countElements(A))