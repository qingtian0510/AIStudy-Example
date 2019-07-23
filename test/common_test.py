import numpy as np

arr = np.arange(1,25,1)
print(arr)
arr = np.reshape(arr,[6,4])
print(arr)
arr = np.split(arr,4,axis=1)
print(arr)