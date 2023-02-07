import re
import os
file_path = r"C:\Users\geniusShi\Desktop\english"

# 有超出utf-8编码的无法处理

def cut_sentences(content):  # 实现分句的函数，content参数是传入的文本字符串
    end_flag = ['?', '!', '.', '？', '！', '。']  # 结束符号，包含中文和英文的
    content_len = len(content)
    sentences = []  # 存储每一个句子的列表
    tmp_char = ''
    for idx, char in enumerate(content):
        tmp_char += char  # 拼接字符
        if (idx + 1) == content_len:  # 判断是否已经到了最后一位
            sentences.append(tmp_char.strip().replace('\ufeff', ''))
            break
        if char in end_flag:  # 判断此字符是否为结束符号
            # 再判断下一个字符是否为结束符号，如果不是结束符号，则切分句子
            next_idx = idx + 1
            if not content[next_idx] in end_flag:
                sentences.append(tmp_char.strip().replace('\ufeff', ''))
                tmp_char = ''

    return sentences  # 函数返回一个包含分割后的每一个完整句子的列表


# for file in os.listdir(file_path):
#     suff_name = os.path.splitext(file)[1]  # 获取文件后缀
#     # 过滤非txt格式文件
#     if suff_name == '.txt':
#         file_name = os.path.splitext(file)[0]  # 获取文件名称
#         path = os.path.join(file_path + '//' + file_name+'.txt')  # 获取文件路径
#         with open(path,"r",encoding='utf-8') as f:
#             content = f.read()
#             print(content)
#             each_sentence = cut_sentences(content)
#             print(each_sentence)
#             path2 = os.path.join(file_path + '//' + file_name + '分句版本.txt')
#             with open(path2, "w", encoding='utf-8') as f:
#                 print(111)
#                 for i in range(len(each_sentence)):
#                     print(each_sentence[i])
#                     f.write(each_sentence[i] + "\n")

def woShiMain():
    get_file_name(file_path)


def get_file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):  # 获取当前文件夹的信息
        print(files)
        for file in files:
            if os.path.splitext(file)[1] == ".txt":  # 提取出所有后缀名为md的文件
                # print(filePath) 绝对路径
                readFile(root, file)


def readFile(root, file):
    oldFilePath = os.path.join(root, file)  # 绝对路径全名
    oldName = os.path.splitext(file)[0]  # 不带后缀
    newFullName = oldName + "分句版本.txt"  # 新全名
    newFilePath = os.path.join(root, newFullName)  # 新绝对路径全名
    with open(oldFilePath, "r", encoding='utf-8') as f:
        content = f.read()
        each_sentence = cut_sentences(content)
        writeFile(newFilePath, each_sentence)


def writeFile(newFilePath, content):
    with open(newFilePath, "w", encoding='utf-8') as f:
        for i in range(len(content)):
            print(content[i])
            f.write(content[i] + "\n")


woShiMain()
