import os

dirpath = 'G:\\eyes\\dizziness_data_txt'
dirs = os.listdir(dirpath)
n = 0
for dir in dirs:
    path = 'G:/eyes/dizziness_data_txt/' + dir
    files = os.listdir(path)
    if files is not None:
        n += 1

print(n)
