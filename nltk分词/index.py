# 导入nltk库
import nltk

# 定义一个句子
sentence = "Owing to the remarkable development in mass-communications, people everywhere are feeling new wants and are being exposed to new customs and ideas, while governments are often forced to introduce still further innovations for the reasons given above."

# 用nltk对句子进行分词，得到一个列表
words = nltk.word_tokenize(sentence)

# 定义一个空字符串，用来存储拼接后的句子
new_sentence = ""

# 定义一个标点符号列表
punctuations = [',', '.', ':', ';', '?', '(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%']

# 用一个循环来遍历列表中的每个单词
for word in words:
    # 判断单词是否是标点符号
    if word in punctuations:
        # 如果是标点符号，就不加上标签
        word = word
    else:
        # 如果不是标点符号，就加上标签
        word = "<span>" + word + "</span>"
    # 将加上标签或者不加标签的单词拼接到新句子中，用空格隔开
    new_sentence = new_sentence + word + " "

# 去掉新句子最后多余的空格
new_sentence = new_sentence.strip()

# 打印新句子
print(new_sentence)