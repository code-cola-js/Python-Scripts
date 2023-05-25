import genanki
import xlrd

my_deck = genanki.Deck(
    2059400110,
    '英语(二) 4500单词')

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
            'name': 'Card 1',
            'qfmt': '{{Question}}<br>',  # AND THIS
            'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}<hr id="text">',
        },
    ])


def read_xlsx():
    workbook = xlrd.open_workbook(r"D:\AFiles\PythonPandocMDToPdf\test.xlsx")
    Words = workbook.sheet_by_name("Sheet1")
    rows = Words.nrows
    print(rows)
    word_list = []

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
    
    my_package.write_to_file("4500.apkg")


if __name__ == '__main__':
    read_xlsx()
