import numpy as np
import cv2
from matplotlib import pyplot as plt

# 创建一个 512×512 的全黑图像
img = np.zeros((512, 512), dtype=np.uint8)

# 在中央绘制一个 200×200 的白色正方形
start = (512 - 200) // 2
end = start + 200
img[start:end, start:end] = 255

# 计算灰度直方图
# cv2.calcHist(images, channels, mask, histSize, ranges)
# - images: 输入图像
# - channels: 灰度图传 [0]
# - mask: None 表示整幅图
# - histSize: 直方图 bin 的数量，灰度级为 256
# - ranges: 像素值范围 [0, 256]
hist = cv2.calcHist([img], [0], None, [256], [0, 256])

# 绘制直方图
plt.figure(figsize=(8, 4))
plt.title("Grayscale Histogram")
plt.xlabel("Gray Level")
plt.ylabel("Number of Pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.grid(True)
plt.show()
