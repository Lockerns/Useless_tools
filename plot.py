import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0.25, 0.6, 0.000001)

y1 = 0.00001/pow(x, 12) - 0.01/pow(x, 6)
y2 = 0.000012/pow(x, 13) - 0.006/pow(x, 7)

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()  # 在x轴绘制第二个y轴

ax1.set_xlabel('r(nm)')
ax1.set_ylabel('Potential Energy, U(r) , J', color='black')
ax1.plot(x, y1, 'black')
ax1.set_ylim(-6, 4)  # 设置y1范围

ax2.set_ylabel('Force, F(r) , N', color='black')
ax2.plot(x, y2, 'red')
ax2.set_ylim(-3, 2)  # 设置y2范围

plt.xlim((0.25, 0.6))  # 设置x范围
plt.show()
# plt.savefig('1.png')
