import numpy as np

arr = np.array(input().strip().split(),float)
np.set_printoptions(sign=' ')
print(np.floor(arr))
print(np.ceil(arr))
print(np.rint(arr))