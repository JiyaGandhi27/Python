def repeatingElement(A, n):

    elements = set()

    for i in A:
        if i in elements:
            return i
        else:
            elements.add(i)
    

A = [1, 2, 4, 3, 2, 1, 4, 7, 9]
n = len(A)
print(repeatingElement(A, n))