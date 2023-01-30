# 该程序用于在复制论文时，删除掉多余的回车
import pyperclip
import time
import re

# 配置正则表达式并读取剪切板
space_d = re.compile(r'\s+')
text = pyperclip.paste()

# 重复读取
while (True):
    read_text = pyperclip.paste()
    if text != read_text:
        # 将多重空格和换行改成单一的空格
        str_new = space_d.sub(' ', read_text)
        # 放回剪切板
        pyperclip.copy(str_new)
        text = pyperclip.paste()
    # 休眠0.5秒
    time.sleep(0.5)
