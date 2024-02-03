import json
import genanki
import xlrd
self_array = []


def read_xlsx():
    workbook = xlrd.open_workbook(
        r"C:\Users\geniusShi\Desktop\01.Excel版本1999-2009分句\1999\Text1.xlsx")
    Words = workbook.sheet_by_name("Sheet1")
    rows = Words.nrows
    word_list = []

    # 便利了excel中 第一行 所有的单词
    for x in range(0, rows):
        self_json = {}
        english = Words.row(x)[0].value
        self_json["english"] = Words.row(x)[0].value
        self_json["translate"] = Words.row(x)[1].value
        self_json["id_number"] = x + ""
        self_array.append(self_json)


if __name__ == '__main__':
    read_xlsx()
    filename = 'pi_x.json'
    with open(filename, 'w') as f:
        json.dump(self_array, f)
