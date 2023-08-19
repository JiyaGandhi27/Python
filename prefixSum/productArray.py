def product(A , n):
    product = 1
    pArray= []
    for i in range(n):
        product = product * A[i]
    for i in range(n):
        pArray.append(product // A[i])
    return pArray      
A = [1, 2, 3, 4, 5]
n = len(A)
print(product(A , n))