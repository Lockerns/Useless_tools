# 此程序用于根据Halcon标定板的参数生成对应的descr文件

def main():
    print('请输入图案边长mm:')
    pattern = input()
    # 计算圆形图案半径
    radius = pattern / 8 / 4


if __name__ == '__main__':
    main()
