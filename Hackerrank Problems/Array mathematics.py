import numpy as np

n,m = map(int, input().split())

arr1 = np.array([input().strip().split() for _ in  range(n)], int)
arr2 = np.array([input().strip().split() for _ in  range(n)], int)

print(arr1 + arr2)
print(arr1 - arr2)
print(arr1 * arr2)
print(arr1 // arr2)
print(arr1 % arr2)
print(arr1 ** arr2)
