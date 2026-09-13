import numpy as np
import cv2

# 创建一个 512×512 的全黑图像（灰度值为 0）
img = np.zeros((512, 512), dtype=np.uint8)

# 在中央绘制一个 200×200 的白色正方形（灰度值为 255）
# 中心点坐标：(256, 256)，左上角点坐标：(156, 156)
start = (512 - 200) // 2        # 156
end = start + 200               # 356

img[start:end, start:end] = 255  # 将中央区域设为白色

# 显示图像
cv2.imshow("Black-White Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 保存图像到当前目录（可选）
cv2.imwrite("black_white.png", img)
