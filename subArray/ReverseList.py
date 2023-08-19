def reverse(A):
    n = len(A)
    start = 0
    end = n-1

    while (start < end):
        A[start] , A[end] = A[end] , A[start]
        start += 1
        end -= 1
    return A

A = [0, 1, 2, 3 ,6 ,9 ,33,28 ]
print(reverse(A))