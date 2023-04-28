import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import brown
 
brown.categories()
s = '近日，中国短道速滑队队员@武大靖,在直播中歪嘴喝水的画面走红,此后他本人还亲自教学。于是，短道速滑国家队的成员们相继挑战,还出了一人炫三瓶的升级版。网友：终于找到进短道速滑队的方法！'
s1 = 'Along with the development of society , more and more problems are brought to our attention , one of the most serious problems is involution and lying flat . Involution means that when social resources cannot meet the needs of everyone, people compete to obtain more resources. An important feature of involution is internal competition , Internal competition is becoming increasing prevalent at an amazing rate. '
englishTokens = word_tokenize(s1)
chineseTokens = word_tokenize(s)
# 分句和分词
print("英文分句", sent_tokenize(s1))
# 遍历sent_tokenize(s1)按照行写入 英文分句.txt
with open('英文分句.txt', 'w') as f:
    for i in sent_tokenize(s1):
        f.write(i + '\n')
        

print("中文分句", sent_tokenize(s))

print("英文分词", englishTokens)
print("中文分句", sent_tokenize(s))
print("中文分词", chineseTokens)
 
# 词性标注
# 分词之后才可以进行词性标注
englishTags = nltk.pos_tag(englishTokens)
chineseTags = nltk.pos_tag(chineseTokens)
print("英文词性标注", englishTags)
print("中文词性标注", chineseTags)
 
# 情感分析
#compound表示复杂程度,neu表示中性,neg表示负面情绪,pos表示正面情绪
from nltk.sentiment.vader import SentimentIntensityAnalyzer
s2 = ['This is a good book', 'This is a bad book']
s3 = ['这是一本好书', '这是一本糟糕的书']
# 创建分类器
sid = SentimentIntensityAnalyzer()
#英文情感分析
for sentence in s2:
    print(sentence)
    print("情感得分", sid.polarity_scores(sentence))
#中文情感分析
for sentence in s3:
    print(sentence)
    print("情感得分", sid.polarity_scores(sentence))