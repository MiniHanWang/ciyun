#@Time:1/6/202112:13 PM
#@Author: Mini(Wang Han)
#@Site:
#@File:ciyun.py

from wordcloud import WordCloud
from scipy.misc import imread
import matplotlib.pyplot as plt
import jieba


def read_deal_text(txt,txt_save):
    with open(txt, "r") as f:  # 读取我们的待处理本文
        txt = f.read()

    re_move = ["，", "。",'\n', '\xa0']  # 无效数据
    # 去除无效数据
    for i in re_move:
        txt = txt.replace(i, " ")
    word = jieba.lcut(txt)  # 使用精确分词模式进行分词后保存为word列表
    with open(txt_save, 'w') as file:
        for i in word:
            file.write(str(i) + ' ')
    print("文本处理完成")
    return
def img_grearte(txt_save,png_save):
    #mask = imread("boy.png")
    with open(txt_save, "r") as file:
        txt = file.read()
    word = WordCloud(background_color="white", \
                     width=800, \
                     height=800,
                     font_path='simhei.ttf',
                     #mask=mask,
                     ).generate(txt)
    word.to_file(png_save)
    print("词云图片已保存")

    plt.imshow(word)  # 使用plt库显示图片
    plt.axis("off")
    plt.show()
txt=r"G:\projects\me\博士\股票\comments\comment.txt"
txt_save=r"G:\projects\me\博士\股票\results\txt_save.txt"
png_save=r'G:\projects\me\博士\股票\results\ciyun.png'
read_deal_text(txt,txt_save)
img_grearte(txt_save,png_save)