# 数字黑洞6174
# 黑洞变换
def blackHole(n):
    print('变换开始')
    while n != 6174:
        # 分解数字
        arr_n = list(str(n))
        # 排列成最大
        n_max = maxNumber(arr_n)
        # 排列成最小
        n_min = minNumber(arr_n)
        # 得到差值
        n = n_max - n_min
        # 打印变换过程
        print("%s-%s=%s" % (n_max, n_min, n))

    print('变换结束')

# 将原数重新排列成最大数
def maxNumber(arr_n):
    arr_n = sorted(arr_n, reverse=True)
    # join是string的方法，所以前面要放到字符串对象后面使用
    max_n = ''.join(arr_n)
    return int(max_n)

# 将原数重新排列成最小数
def minNumber(arr_n):
    arr_n = sorted(arr_n, reverse=False)
    min_n = ''.join(arr_n)
    return int(min_n)

# 检查输入的数字是否合格——是否都是数字，是否长度为4，是否不全相同
def checkNum(_num):
    if not _num.isdigit():
        return False
    elif len(_num) != 4:
        return False
    elif _num == _num[0]*4:
        return False
    else:
        return True

def main():
    while True:
        num = input('请输入一个4位整数，4个数字不能完全相同：')
        if checkNum(num):
            blackHole(num)
            break
        else:
            print('输入内容不合法，请重新输入')
            continue


if __name__ == '__main__':
    main()
