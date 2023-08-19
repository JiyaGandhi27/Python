def rotate(A):
    n = len(A)
    start = 0 
    end  = n - 1
    B = 4

    while (start < end):
        A[start] , A[end] = A[end] , A[start]
        start += 1
        end -= 1

    start = 0
    end  = B - 1
    while (start < end):
        A[start] , A[end] = A[end] , A[start]
        start += 1
        end -= 1

    start = B
    end  = n - 1
    while (start < end):
        A[start] , A[end] = A[end] , A[start]
        start += 1
        end -= 1
    return A

A = [ 1, 2, 3, 4, 5, 6, 7, 8 ]
print(rotate(A))