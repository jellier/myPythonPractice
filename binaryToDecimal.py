# 二进制十进制互换

def decimal2binary():
    # 十进制转换为二进制
    e = [0, 0, 0, 0, 0, 0, 0, 0]
    s = int(input("请输入一个十位数："))
    for i in range(0, 8, 1):
        e[i] = int(s % 2)
        s = s // 2
    e.reverse()
    print("二进制数为：", e)


def binary2decimal():
    # 二进制转换为十进制
    s = [0, 0, 0, 0, 0, 0, 0, 0]
    a = 0
    s = list(input("请输入一个二进制数："))
    s.reverse()
    for i in range(0, len(s), 1):
        if int(s[i]) == 1:
            a += pow(2, i)
    print("十进制数是：", a)


while True:
    # choose = int(input("二进制转十进制请输入10\n十进制转二进制请输入2\n"))
    # if choose == 10:
    #     binary2decimal()
    # elif choose == 2:
    #     decimal2binary()
    # else:
    #     break
    binary2decimal()