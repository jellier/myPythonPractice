# 将彩色图像转换成字符画
# 使用到pillow库

from PIL import Image

def main():
    img_Harry = 'image/HarryPotter.jpg'
    width,height = 100, 60
    # resize方法的参数必须是元组
    # convert方法转换图像的颜色模式，L代表灰度图像，RGB表示真彩色图像，CMYK表示出版图像
    # open\resize\convert 方法均返回图像对象，可用链式写法
    img_new = Image.open(img_Harry).resize((width,height)).convert('L')

    # 将每个像素转成字符
    text = ''
    for y in range(height):
        for x in range(width):
            text += getchar(img_new.getpixel((x, y)))
        text += '\n'

    # 存储图像到记事本
    temp = open('PIL_HarryPotter.txt','w')
    temp.write(text)
    temp.close()


# 根据灰度值返回字符
def getchar(gray):
    # return '@' if gray < 128 else ' '

    # MNHQ$OC?7>!:-;.是一个常用的效果较好的灰度字符序列
    ascii_chars = list('MNHQ$OC?7>!:-;.')
    slen = 256/len(ascii_chars)
    return ascii_chars[int(gray//slen)]


if __name__ == '__main__':
    main()