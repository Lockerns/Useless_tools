# 该程序用于在复制论文时，删除掉多余的回车
import pyperclip
import time
import re

# 配置正则表达式并读取剪切板
space_d = re.compile(r'\s+')
text = pyperclip.paste()
print(len(text))
