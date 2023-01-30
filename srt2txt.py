# 该程序用于将srt字幕转换为普通文本，即删除时间戳
# 读取srt文件内容到datalist
with open('./sleep.srt') as f:
    datalist = f.readlines()
    num = len(datalist)
    f.close()

# 将需要的文本重新写入新的文件.txt
f = open('./Deep_Sleep.txt', 'w')
for i in range(num):
    if (i - 2) % 4 == 0:
        f.write(datalist[i])
f.close()
