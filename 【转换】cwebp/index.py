import os


def get_file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):  # 获取当前文件夹的信息
        # print(root)
        # print(dirs)
        # print(files)
        for file in files:  
            # 提取出所有后缀名为png, jpeg, jpg的文件
            if os.path.splitext(file)[1] == ".png" or os.path.splitext(file)[1] == ".jpeg" or os.path.splitext(file)[1] == ".jpg":
                # print(root)
                os.chdir(root)

                print("转换开始：" + "cwebp " + file + " -o " +
                      os.path.splitext(file)[0] + ".webp")
                # 使用os.system调用cwebp进行格式转化
                os.system("cwebp " + file + " -o " +
                          os.path.splitext(file)[0] + ".webp")
                print("转换完成...")


if __name__ == "__main__":
    get_file_name(
        r"C:\Users\Administrator\Desktop\images")  # 修改文件路径
