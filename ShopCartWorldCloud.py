from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba

# 词云使用特殊形状的轮廓需要numpy和pillow, 如客户端不支持可以去掉
from PIL import Image
import numpy as np

# 步骤1：使用os导入文件中的信息
# 注意编码问题
d = path.dirname(__file__)
text = open(path.join(d,  "image/shopcart.txt")).read()

# 步骤2：使用jieba分词
textlist = jieba.lcut(text)
string = " ".join(textlist)
print(textlist)

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
plt.imshow(wordcloud,  interpolation="bilinear")
# 步骤4-3：取消图表x、y轴
plt.axis("off")
# 显示图片
plt.show()

counts={}
child=['儿童', '宝宝', '青少年', '幼儿', '中大童', '小童', '男孩', '女孩', '12 ', '7 ', '15 ', '3 ', '4 ', '5', '亲子']
adult = ['男', '女', '妈妈', '爸爸', '成人', '中老年']
food =['早餐', '代餐 ', '饱腹 ', '食品 ', '五谷杂粮', '粗粮 ', '小吃', '主食', '零食', '奶酪 ', '烘焙', '海鲜', '糖果']
toy =['滑板车 ', '闪光']
book=['进口 ', '小说 ', '桥梁 ', '书', '英文原版 ', '全彩', '卡通', '启蒙 ', '绘本 ', '图画书 ', '新华 ', '正版', '数学 ', '书籍', '平装 ', '套装', '系列 ', '全套']
cloth = ['套头毛衣 ', '线衣 ', '针织 ', '上衣', '纯棉', '羽绒服']
family = ['户外 ', '手推车 ', '家居服']
rword = '其他'
for word in textlist:
    # 去标点符号
    if word == ' ':
        continue
    elif word in child or word in toy or word in book:
        rword = '孩子'
    elif word in adult or word in cloth:
        rword = '大人'
    elif word in food or word in family:
        rword = '全家'

    counts[rword] = counts.get(rword,  0) + 1
print(counts)