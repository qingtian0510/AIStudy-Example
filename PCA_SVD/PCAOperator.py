import numpy as np
import pandas as pb
import matplotlib as plt

df = pb.read_csv('iris.csv')

df.cloumns=['sepal_len','sepal_wid','petal_len','petal_wid','class']

X = df.ix[:,1:5].values
Y = df.ix[:,5].values

from sklearn.preprocessing import StandardScaler
X_std = StandardScaler().fit_transform(X) #数据标准化

mean_vec = np.mean(X_std,axis=0)

cov_mat = (X_std-mean_vec).T.dot(X_std-mean_vec)/(X_std.shape[0]-1) #计算协方差矩阵
#print(cov_mat)
#print(np.cov(X_std.T))   numpy提供了直接计算协方差矩阵的方法

eig_vals,eig_vecs = np.linalg.eig(cov_mat) #计算矩阵的特征值和特征向量
# print(eig_vals)
# print(eig_vecs)

eig_pairs = [(np.abs(eig_vals[i]),eig_vecs[:,i]) for i in range(len(eig_vals))]  #将特征值和特征向量组成一对一对
# print(eig_pairs)

eig_pairs.sort(key=lambda x:x[0],reverse=True) #特征值特征向量对按照特征值大小降序排列

matrix_w = np.hstack((eig_pairs[0][1].reshape(4,1),eig_pairs[1][1].reshape(4,1)))
# print(matrix_w)
Y = X_std.dot(matrix_w)
# print(Y)

# plt.figure((6,4))
# for lab,col in zip(('setosa','versicolor','virginica'),('blue','red','green')):
#     plt.scatter(X[y==lab,0],X[y==lab,1],label=lab,c=col)
# plt.xlabel('sepal_len')
# plt.ylabel('sepal_wid')
# plt.legend(loc='best')
# plt.tight_layout()
# plt.show()