import numpy as np


data = [[1,1,1,0,0],
        [2,2,2,0,0],
        [1,1,1,0,0],
        [5,5,5,0,0],
        [1,1,0,2,2],
        [0,0,0,3,3],
        [0,0,0,1,1]]


U,Sigma,VT = np.linalg.svd(data)

sig3 = np.mat([[Sigma[0],0,0],[0,Sigma[1],0],[0,0,Sigma[2]]])

data_new = U[:,:3]*sig3*VT[:3,:]
print(data_new)