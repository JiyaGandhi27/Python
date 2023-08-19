def repeatingElement(A, n):

    elements = {}
    
    for value in A:
        if value in elements:
            elements[value] += 1
        else:
            elements[value] = 1

    for i in range(n):
        if elements.get(A[i]) > 1:
            return A[i] 

A = [1, 2, 4, 3, 2, 1, 4, 7, 9]
n = len(A)
print(repeatingElement(A, n))