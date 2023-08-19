#amazing subarray - 
#length of subarray is even and sum is less than B
#length of subarray is odd and sum is greater than B
#Find the no. of amazing subarrays

def prefixSum(A, n):
    PS = []
    PS.append(A[0])
    for i in range(1, n):
        PS.append(PS[i-1] + A[i])
    return PS

def subArrayLength(A, n):
    PS = []
    PS = prefixSum(A,n)
    subArray = []
    b = 4
    count = 0

    for i in range(n):
        sum = 0
        for j in range(i, n):
            length = j - i + 1
            subArray.append(length)
            if j == 0:
                sum = PS[i]
            else:
                sum = PS[i] - PS[j-1]

            if (length % 2 == 0) and (sum < b):
                count += 1
            elif (length % 2 != 0) and (sum > b):
                count +=1
            else:
                count = count

    print(count)

A = [1, 2, 3]
n =len(A)
subArrayLength(A, n)