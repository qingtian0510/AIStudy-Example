from scipy import ndimage
import numpy as np
import matplotlib.pyplot as plt


def pic_compress(k, pic_array):
    u, sigma, vt = np.linalg.svd(pic_array)
    sig = np.eye(k) * sigma[: k]
    new_pic = np.dot(np.dot(u[:, :k], sig), vt[:k, :])  # 还原图像
    size = u.shape[0] * k + sig.shape[0] * sig.shape[1] + k * vt.shape[1]  # 压缩后大小
    return new_pic, size


path = './1.jpeg'
ori_img = np.array(ndimage.imread(path, flatten=True))


new_img, size = pic_compress(30, ori_img)
print("original size:" + str(ori_img.shape[0] * ori_img.shape[1]))
print("compress size:" + str(size))

print(size)
fig, ax = plt.subplots(1, 2)
ax[0].imshow(ori_img)
ax[0].set_title("before compress")
ax[1].imshow(new_img)
ax[1].set_title("after compress")
plt.show()

# #data = np.mat(img)
# print(ori_img.shape())
# # 需要mat处理后才能在降维中使用矩阵的相乘
# U, sigma, VT = np.linalg.svd(data)
# # 在重构之前，依据前面的方法需要选择达到某个能量度的奇异值
# cnt = sum(sigma)
# print(cnt)
# cnt90 = 0.9 * cnt  # 达到90%时的奇异总值
# print(cnt90)
# count = 50  # 选择前50个奇异值
# cntN = sum(sigma[:count])
# print(cntN)
#
# # 重构矩阵
# dig = np.mat(np.eye(count) * sigma[:count])  # 获得对角矩阵
# # dim = data.T * U[:,:count] * dig.I # 降维 格外变量这里没有用
# redata = U[:, :count] * dig * VT[:count, :]  # 重构
#
# plt.imshow(data, cmap='gray')  # 取灰
# plt.show()  # 可以使用save函数来保存图片
