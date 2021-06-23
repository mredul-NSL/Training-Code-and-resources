import numpy

arr = list(map(float, input().split()))

x = float(input())

print(numpy.polyval(arr, x))