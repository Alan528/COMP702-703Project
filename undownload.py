import os

def del_file():
    files = os.listdir(".")

    for file in files:
        if '.' in file:
            suffix = file.split('.')[-1]
            # 指定删除ev4的后缀名文件
            if suffix == 'mp3' or suffix == 'mp4':
                os.remove(os.path.join(".", file))


