import os

needmodify = []

def get_file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):  # 获取当前文件夹的信息
        # print(files)
        print(files)
        for file in files:
            # print(file)# 扫描所有文件
            if os.path.splitext(file)[1] == ".txt":  # 提取出所有后缀名为html的文件
                bbb = os.path.join(root, file)
                needmodify.append(bbb)


def modifyself(seltlist):
    for i in range(len(seltlist)):
        newName = os.path.splitext(seltlist[i])[0] + ".doc"
        os.rename(seltlist[i], newName)


if __name__ == "__main__":
    get_file_name(r"C:\Users\geniusShi\Desktop\1999") # 修改文件路径
    modifyself(needmodify)