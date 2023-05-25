import nltk
import re
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import brown
 
brown.categories()
s = '近日，中国短道速滑队队员@武大靖,在直播中歪嘴喝水的画面走红,此后他本人还亲自教学。于是，短道速滑国家队的成员们相继挑战,还出了一人炫三瓶的升级版。网友：终于找到进短道速滑队的方法！'
s1 = '''
“The Heart of the Matter,” the just-released report by the American Academy of Arts and Sciences (AAAS), deserves praise for affirming the importance of the humanities and social sciences to the prosperity and security of liberal democracy in America.
Regrettably, however, the report's failure to address the true nature of the crisis facing liberal education may cause more harm than good.
In 2010, leading congressional Democrats and Republicans sent letters to the AAAS asking that it identify actions that could be taken by "federal, state and local governments, universities, foundations, educators, individual benefactors and others" to "maintain national excellence in humanities and social scientific scholarship and education.
"In response, the American Academy formed the Commission on the Humanities and Social Sciences.
Among the commission's 51 members are top-tier-university presidents, scholars, lawyers, judges, and business executives, as well as prominent figures from diplomacy, filmmaking, music and journalism.
The goals identified in the report are generally admirable.
Because representative government presupposes an informed citizenry, the report supports full literacy; stresses the study of history and government, particularly American history and American government; and encourages the use of new digital technologies.
To encourage innovation and competition, the report calls for increased investment in research, the crafting of coherent curricula that improve students' ability to solve problems and communicate effectively in the 21st century, increased funding for teachers and the encouragement of scholars to bring their learning to bear on the great challenges of the day.
The report also advocates greater study of foreign languages, international affairs and the expansion of study abroad programs.
Unfortunately, despite 2 years in the making, "The Heart of the Matter" never gets to the heart of the matter: the illiberal nature of liberal education at our leading colleges and universities.
The commission ignores that for several decades America's colleges and universities have produced graduates who don't know the content and character of liberal education and are thus deprived of its benefits.
Sadly, the spirit of inquiry once at home on campus has been replaced by the use of the humanities and social sciences as vehicles for publicizing "progressive," or left-liberal propaganda.
Today, professors routinely treat the progressive interpretation of history and progressive public policy as the proper subject of study while portraying conservative or classical liberal ideas—such as free markets or self-reliance —as falling outside the boundaries of routine, and sometimes legitimate, intellectual investigation.
The AAAS displays great enthusiasm for liberal education.
Yet its report may well set back reform by obscuring the depth and breadth of the challenge that Congress asked it to illuminate.
'''
englishTokens = word_tokenize(s1)
chineseTokens = word_tokenize(s)
# 分句和分词
print("英文分句", sent_tokenize(s1))
# 遍历sent_tokenize(s1)按照行写入 英文分句.txt, utf-8编码
with open('英文分句.txt', 'w', encoding='utf-8') as f:
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