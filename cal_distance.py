# 本程序用于计算像素距离和实际距离的对应关系
import math
# 靶面对角线长度（inch）
diagonal_mm = 16/2.8

# 宽高比
width = 4
height = 3
diagonal = pow(width * width + height * height, 0.5)

# 计算靶面宽高
width_b = diagonal_mm * width / diagonal
height_b = diagonal_mm * height / diagonal

# 焦距和距离
f = 2.8
d = 10 * 1000
# 分辨率设置
w = [1080, 1920, 2560, 4096]
h = [720, 1080, 1440, 2160]

for i in range(4):
    # 单个像素宽度
    wp = width_b / w[i]
    # 所求实际距离
    x = d * wp / f
    print('在{} x {}分辨率下,单个像素对应的实际宽为:{:.2f}mm'.format(w[i], h[i], x))

# 视场角
b = 2 * math.atan(width_b/(2 * f))  # 计算弧度
a = b / math.pi * 180  # 弧度转化为角度
print('视场角:{:.2f}度'.format(a))
