# 数字黑洞6174

def blackHole(n):
    print('计算开始')
    while n != 6174:
        arr_n = list(str(n))
        n_max = maxNumber(arr_n)
        n_min = minNumber(arr_n)
        n = n_max - n_min
        print("%s-%s=%s" % (n_max, n_min, n))

    print('计算结束')


def maxNumber(arr_n):
    arr_n = sorted(arr_n, reverse=True)
    max_n = ''.join(arr_n)
    return int(max_n)


def minNumber(arr_n):
    arr_n = sorted(arr_n, reverse=False)
    min_n = ''.join(arr_n)
    return int(min_n)


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
