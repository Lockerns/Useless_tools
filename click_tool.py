# 循环点击选中的两个点
import pyautogui
import time


def click_L(x, y):
    pyautogui.click(x, y)


def main():
    pyautogui.PAUSE = 0.5
    pyautogui.FAILSAFE = True
    # input()
    # x1, y1 = pyautogui.position()
    # print(x1)
    # print(y1)
    # input()
    # x2, y2 = pyautogui.position()
    # print(x2)
    # print(y2)
    x1 = 983
    y1 = 516
    x2 = 1118
    y2 = 516
    while (True):
        click_L(x1, y1)
        # time.sleep(0.15)
        click_L(x2, y2)
        time.sleep(0.05)


if __name__ == '__main__':
    main()
