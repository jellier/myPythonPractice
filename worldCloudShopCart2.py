from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba

# 词云使用特殊形状的轮廓需要numpy和pillow,如客户端不支持可以去掉
from PIL import Image
import numpy as np

# 步骤1：使用os导入文件中的信息
# 注意编码问题
d = path.dirname(__file__)
text = open(path.join(d, "image/shopcart.txt")).read()

# 步骤2：使用jieba分词
textlist = jieba.lcut(text)
string = " ".join(textlist)

# 步骤3：设置一张词云图对象
bg = np.array(Image.open("image/shop.jpg"))
wordcloud = WordCloud(
    background_color="white",
    max_font_size=40,
    mask=bg,
    font_path='image/NotoSansHans-Black.otf'
).generate(string)
# 步骤4：使用 matplotlib 显示图片
# 步骤4-1：创建一个图表画布
plt.figure()
# 步骤4-2：设置图片
plt.imshow(wordcloud, interpolation="bilinear")
# 步骤4-3：取消图表x、y轴
plt.axis("off")
# 显示图片
plt.show()
