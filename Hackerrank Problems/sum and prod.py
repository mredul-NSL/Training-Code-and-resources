import numpy as np 

n,m = map(int, input().split())

arr = np.array([input().strip().split() for _ in range(n)],int)

arr = np.sum(arr, axis = 0)

print(np.prod(arr))

