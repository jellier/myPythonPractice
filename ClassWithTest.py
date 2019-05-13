# 抛出异常和类的结合
# python中的with语句使用于对资源进行访问的场合，保证不管处理过程中是否发生错误或者异常都会执行规定的__exit__（“清理”）操作，释放被访问的资源
# 比如有文件读写后自动关闭、线程中锁的自动获取和释放等。

class Testwith():
    # __enter__ 和__exit__为类的内置方法，当类开始和结束时执行
    def __enter__(self):
        print('enter class TestWith')

    def __exit__(self, exc_type, exc_val, exc_tb):  # 参数为默认参数
        if exc_tb is None:  # this means exc_tb == None
            print('class is over')
        else:
            print('Error! errormessage is %s' % exc_tb)


with Testwith():
    print('Test is running')
    # raise是抛出异常时使用的方法
    raise NameError('testNameError')
