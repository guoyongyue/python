from os import path

from scipy.misc import imread
import matplotlib.pyplot as plt
import jieba
# jieba.load_userdict("txt\userdict.txt")
# 添加用户词库为主词典,原词典变为非主词典
from wordcloud import WordCloud, ImageColorGenerator

# 获取当前文件路径
# __file__ 为当前文件, 在ide中运行此行会报错,可改为
# d = path.dirname('.')
d = path.dirname(__file__)

stopwords = {}
isCN = 1 #默认启用中文分词
back_coloring_path = "E:/work/github/python/Demo/source/img/source/002.jpg" # 设置背景图片路径
text_path = 'E:/work/github/python/Demo/source/file/test.txt' #设置要分析的文本路径
font_path = 'D:/Fonts/simkai.ttf' # 为matplotlib设置中文字体路径没
stopwords_path = 'E:/work/github/python/Demo/source/file/stopwords.txt' # 停用词词表
imgname1 = "E:/work/github/python/Demo/source/img/save/save.png" # 保存的图片名字1(只按照背景图片形状)
imgname2 = "E:/work/github/python/Demo/source/img/save/save2.png"# 保存的图片名字2(颜色按照背景图片颜色布局生成)

my_words_list = ['孙金博','王华柱','王少卿','方涛','李壮壮','王鸿资','王良田','陈博文','赵振宇','周文博','刘晓松','刘亦鸣',
                 '史晨方','燕高远','赵振','周巨擘','冯璐毅','井诚','李昶樟','刘冉冉','马雨涵','徐硕','杨帅','周正','李员琦',
                 '卢荟锦','吕兆凯','谢亚茹','张哲','刘雨晴','庄艺','王高鹏','王宁博','黄聪','张世兴','毛金玉','朱志良',
                 '田晓东','赵志鹏','梁帅阳','刘纪伟','陈建业','韩文超','张镕己','许立为','廖呈锋','田家豪','付荣伟','黄晓方',
                 '魏鹏昊','鲁启明','鲁长昊','鲁甲豪','訾书鉴',
                 '李启明','张魁','姚大林','张莉柯','穆天宇','魏士恩','吕志远','张俊涛',
                 '刘明轩','宋睿栋','王钧仕','刘电科','徐守壮','张羽飞','袁亚南','金文庆'] # 在结巴的词库中添加新词

back_coloring = imread(path.join(d, back_coloring_path))# 设置背景图片

# 设置词云属性
wc = WordCloud(font_path=font_path,  # 设置字体
               background_color="white",  # 背景颜色
               max_words=2000,  # 词云显示的最大词数
               mask=back_coloring,  # 设置背景图片
               max_font_size=100,  # 字体最大值
               random_state=42,
               width=1000, height=860, margin=2,# 设置图片默认的大小,但是如果使用背景图片的话,那么保存的图片大小将会按照其大小保存,margin为词语边缘距离
               )

# 添加自己的词库分词
def add_word(list):
    for items in list:
        jieba.add_word(items)

add_word(my_words_list)

text = open(path.join(d, text_path), 'rb').read()

def jiebaclearText(text):
    mywordlist = []
    seg_list = jieba.cut(text, cut_all=False)
    liststr="/ ".join(seg_list)
    f_stop = open(stopwords_path, 'rb')
    try:
        f_stop_text = f_stop.read()
        f_stop_text=f_stop_text.decode('utf-8')
    finally:
        f_stop.close( )
    f_stop_seg_list=f_stop_text.split('\n')
    for myword in liststr.split('/'):
        if not(myword.strip() in f_stop_seg_list) and len(myword.strip())>1:
            mywordlist.append(myword)
    return ''.join(mywordlist)

if isCN:
    text = jiebaclearText(text)

# 生成词云, 可以用generate输入全部文本(wordcloud对中文分词支持不好,建议启用中文分词),也可以我们计算好词频后使用generate_from_frequencies函数
wc.generate(text)
# wc.generate_from_frequencies(txt_freq)
# txt_freq例子为[('词a', 100),('词b', 90),('词c', 80)]
# 从背景图片生成颜色值
image_colors = ImageColorGenerator(back_coloring)

plt.figure()
# 以下代码显示图片
plt.imshow(wc)
plt.axis("off")
plt.show()
# 绘制词云

# 保存图片
wc.to_file(path.join(d, imgname1))

image_colors = ImageColorGenerator(back_coloring)

plt.imshow(wc.recolor(color_func=image_colors))
plt.axis("off")
# 绘制背景图片为颜色的图片
plt.figure()
plt.imshow(back_coloring, cmap=plt.cm.gray)
plt.axis("off")
plt.show()
# 保存图片
wc.to_file(path.join(d, imgname2))
