import numpy as np

# 创建图像矩阵（3行3列）
img = np.array([[2, 4, 5, 6],
                [3, 1, 5, 3],
                [6, 2, 2, 2]])

# 计算平均灰度值：所有像素之和 / 像素总数
average = img.sum() / img.size

# 输出结果
print("图像矩阵：")
print(img)
print("平均灰度值为：", average)