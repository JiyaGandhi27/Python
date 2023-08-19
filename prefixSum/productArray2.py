def Product(A , n):
    PA = []
    PA.append(A[0])
    for i in range(1, n):
        PA.append(PA[i-1]*A[i])

    SA = []
    for i in range(len(A)):
        SA.append(1)
    SA[n-1] = A[n-1]
    for i in range(n-2,-1,-1):
        SA[i] = SA[i+1] * A[i]

    Product = []
    for i in range(n):
        if i == 0:
            Product.append(SA[i+1])
        elif i == n-1:
            Product.append(PA[i-1])
        else:
            Product.append(PA[i-1]*SA[i+1])
    
    return Product



A = [1, 2, 3, 4, 5]
n = len(A)
print(Product(A , n))



