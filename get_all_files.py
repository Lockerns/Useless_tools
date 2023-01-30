import os


def all_files_path(rootDir):
    for root, dirs, files in os.walk(rootDir):
        for file in files:  # 遍历文件
            file_name, extension = os.path.splitext(file)
            if extension == '.avi':  # 判断是否是视频
                file_path = os.path.join(root, file)  # 获取文件绝对路径
                filepaths.append(file_path)  # 将文件路径添加进列表
                filepaths.append(file_name)  # 将视频名添加进列表


if __name__ == "__main__":
    filepaths = []  # 初始化列表
    # 文件所在根目录
    dirpath = 'G:\\eyes\\data'
    all_files_path(dirpath)
    with open('G:\\eyes\\output\\dir_f.txt', 'a') as f:
        for filepath in filepaths:
            c_path = filepath.replace('\\', '/')  # 文件路径中的\换成/
            f.write(c_path + '\n')
