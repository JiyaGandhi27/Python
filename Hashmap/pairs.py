def pairs(A, k):
    count = 0
    freqMap = {}

    for i in A:
        freqMap[i] = freqMap.get(1, 0) + 1

    for i in A:
        diff = i + k

        if diff in freqMap and freqMap[diff]> 0:
            count += freqMap.get(diff)

    return count

A = [1, 5, 3, 4, 2]
k = 2
print(pairs(A, k))