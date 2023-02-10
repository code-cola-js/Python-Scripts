import genanki
import xlrd
import os
rootPath = r"C:\Users\geniusShi\Desktop\1999-2009分句\1999"





# anki 的牌model 可以根据自己的想法设置
my_model = genanki.Model(
    1091735104,
    'Simple Model with Media',
    # 这里是传入fields 的变量代名
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
    ],
    # 直接将你传入的 变量 通过代名 写入模版 html还是很好理解的
    templates=[
        {
            'name': 'Card 1',  # 卡片名字
            'qfmt': '<div id="python-front">{{Question}}</div><br>',  # AND THIS
            'afmt': '{{FrontSide}}<hr id="answer"><div id="python-back">{{Answer}}</div>',
        },
    ],
    css='#python-front{font-size: 20px} #python-back{font-size:20px}'
    )


def read_xlsx(path, file_name, path2):
    workbook = xlrd.open_workbook(path)
    Words = workbook.sheet_by_name("Sheet1")
    rows = Words.nrows
    print(rows)
    word_list = []
    my_deck = genanki.Deck(
    2059400110,
    file_name)  # 卡组名字
    # 便利了excel中 第一行 所有的单词
    for x in range(0, rows):
        # 获得第一列的内容
        first_str = Words.row(x)[0].value
        # 获得第二列的内容
        second_str = Words.row(x)[1].value
        my_note = genanki.Note(
            model=my_model,
            fields=[first_str, second_str])

        my_deck.add_note(my_note)
    print('list:', word_list)
    my_package = genanki.Package(my_deck)

    my_package.write_to_file(path2)
    
def batchExe(rootPath):
  for file in os.listdir(rootPath):
    suff_name = os.path.splitext(file)[1]  # 获取文件后缀
    if suff_name == '.xlsx':
        file_name = os.path.splitext(file)[0]  # 获取文件名称
        path = os.path.join(rootPath + '//' + file_name+'.xlsx')  # 获取文件路径
        path2 = os.path.join(rootPath + '//' + file_name+'.apkg')  # 获取文件路径
        read_xlsx(path, file_name, path2)


if __name__ == '__main__':
    batchExe(rootPath)
