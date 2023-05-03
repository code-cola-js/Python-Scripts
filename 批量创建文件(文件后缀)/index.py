import os
filePrefix = '1999' #文件前缀
fileSuffix = '.txt' #文件后缀
fileNum = 11 #文件个数
for i in range(fileNum):
    # filePrefix转为数字与i相加后再转为字符串
    fileName = str(int(filePrefix) + i) + fileSuffix
    with open(fileName, 'w') as f:
        f.write('')