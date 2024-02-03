import spacy

nlp = spacy.load('en_core_web_sm')  # 加载英文模型
doc = nlp("This is a sentence to be split into phrases.")  # 输入句子

phrases = []
for sent in doc.sents:  # 遍历所有句子
    phrase = ""
    for token in sent:  # 遍历句子中的所有单词
        if token.dep_ == "punct":  # 忽略标点符号
            continue
        if phrase == "":  # 新建词组
            phrase = token.text
        elif token.pos_ == "VERB" or token.pos_ == "ADP":  # 以动词或介词为分界点，结束当前词组
            phrases.append(phrase)
            phrase = token.text
        else:  # 继续添加单词
            phrase += " " + token.text
    phrases.append(phrase)  # 将最后一个词组添加到列表中

print(phrases)  # 输出分割后的词组列表
