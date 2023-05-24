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

each_Card_first_str = []

each_Card_Tags = []

def add_To_Anki():
    for i in range(len(each_Card_first_str)):
        my_note = genanki.Note(
            model=my_model,
            fields=[each_Card_first_str[i], each_Card_Tags[i]])

        my_deck.add_note(my_note)
    my_package = genanki.Package(my_deck)
    my_package.write_to_file("4500.apkg")



def read_txt():
    with open(r"test.txt", "r", encoding="utf-8-sig") as f:
        lines = f.read().splitlines()
        for i, line in enumerate(lines):
            line = line.replace('\ufeff', '')

            first_str = ''
            tags = ''
            if(i % 5 == 0):
                each_Card_Tags.append(line)
            if(i % 5 == 3):
                each_Card_first_str.append(line)
    add_To_Anki()




if __name__ == '__main__':
    read_txt()

