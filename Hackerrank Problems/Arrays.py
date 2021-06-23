import numpy

def arrays(arr):
    arr = list(reversed(arr))
    for i in range (len(arr)):
        arr[i] = float(arr[i])
    return numpy.array(arr)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)