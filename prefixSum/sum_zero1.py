def sum_zero(A, n):
    elements = set()
    sum = 0 
    for i in range(n):
        sum += A[i]
        if sum == 0 or sum in elements:
            return True
        else:
            elements.add(sum)
    return False
A = [1, -1, 3, 2]
n = len(A)
print(sum_zero(A, n))