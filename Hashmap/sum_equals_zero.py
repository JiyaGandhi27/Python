def sumZero(A, n):
    hashmap = set()
    sum = 0
    count = 0

    for i in range(n):
        sum += A[i]
        if sum == 0 or sum in hashmap:
            count += 1
    print(count)
    
A = [1, 0, 1]
n = len(A)
sumZero(A, n)