#check key values

A = {"key1": "value1", 34: 1, 56: 0}

if 34 in A:
    value = A[34]
    print(value)
else:
    print("Key not found")
