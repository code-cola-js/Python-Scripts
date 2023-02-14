import json
import genanki
import xlrd
import os
self_array = []

rootPath = r"C:\Users\geniusShi\Desktop\01.Excel版本1999-2009分句\1999"


def read_xlsx(path ,path2):
    workbook = xlrd.open_workbook(path)
    Words = workbook.sheet_by_name("Sheet1")
    rows = Words.nrows

    # 便利了excel中 第一行 所有的单词
    for x in range(0, rows):
        self_json = {}
        english = Words.row(x)[0].value
        self_json["id_number"] = str(x)
        self_json["english"] = Words.row(x)[0].value
        self_json["translate"] = Words.row(x)[1].value
        self_array.append(self_json)
        with open(path2, 'w') as f:
            json.dump(self_array, f)


if __name__ == '__main__':
    for file in os.listdir(rootPath):
        suff_name = os.path.splitext(file)[1]  # 获取文件后缀
        if suff_name == '.xlsx':
            file_name = os.path.splitext(file)[0]  # 获取文件名称
            path = os.path.join(rootPath + '//' + file_name+'.xlsx')  # 获取文件路径
            path2 = os.path.join(rootPath + '//' + file_name+'.json')  # 获取文件路径
            read_xlsx(path, path2)

