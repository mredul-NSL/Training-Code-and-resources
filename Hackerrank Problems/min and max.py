import numpy as np

import numpy as np 

n,m = map(int, input().split())

arr = np.array([input().strip().split() for _ in range(n)],int)

arr = np.min(arr, axis = 1)

print(np.max(arr))

