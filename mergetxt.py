import os
# 获取目标文件夹的路径
meragefiledir = './src'
# 获取当前文件夹中的文件名称列表
filenames = os.listdir(meragefiledir)
# 获取输出文件的路径
file = open('./code.txt', 'w')
# 向文件中写入字符
# file.write('test\n')

for filename in filenames:
    filepath = meragefiledir+'\\'+filename
    for line in open(filepath):
        file.writelines(line)
    file.write('\n')

file.close()
