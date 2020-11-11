import jieba
# 用来获取文档的路径
from os import path
# 词云
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
# 词云生成工具
from wordcloud import WordCloud, ImageColorGenerator
# 需要对中文进行处理
import matplotlib.font_manager as fm

# 背景图
bg = np.array(Image.open("image/hlw.jpg"))

# 获取当前的项目文件加的路径
d = path.dirname(__file__)

# 读取要分析的文本
text_path = "sanguo_book.txt"
# 读取要分析的文本，读取格式
text = open(path.join(d, text_path), encoding="GB18030").read()

textlist = jieba.lcut(text)
text1 = " ".join(textlist)


# 生成
wc = WordCloud(
    background_color="white",
    max_words=150,
    mask=bg,  # 设置图片的背景
    max_font_size=60,
    random_state=42,
    font_path='image/NotoSansHans-Black.otf'  # 中文处理，用系统自带的字体
).generate(text1)
# 为图片设置字体
my_font = fm.FontProperties(fname='image/NotoSansHans-Black.otf')
# 产生背景图片，基于彩色图像的颜色生成器
image_colors = ImageColorGenerator(bg)
# 开始画图
plt.imshow(wc, interpolation="bilinear")
# 为云图去掉坐标轴
plt.axis("off")
# 画云图，显示
# plt.figure()
plt.show()
# 为背景图去掉坐标轴
plt.axis("off")
plt.imshow(bg, cmap=plt.cm.gray)
# plt.show()

# 保存云图
wc.to_file("image/sanguo.png")
