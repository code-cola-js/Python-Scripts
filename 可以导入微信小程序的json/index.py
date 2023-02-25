import json
import glob

# 所有要合并的json文件所在的文件夹路径
folder_path = r"C:\Users\geniusShi\Desktop\01.Excel版本1999-2009分句\2009"

# 读取所有json文件
json_files = glob.glob(folder_path + '/*.json')

# 用于存储所有JSON数据的列表
all_data = []

# 循环读取每个JSON文件
for file in json_files:
    print(file)
    with open(file, 'r') as f:
        data = json.load(f)
        # all_data.append(data)
        with open(folder_path + 'merge' +'.json', 'a') as f:
            json.dump(data, f)

# 将所有JSON数据写入新文件
