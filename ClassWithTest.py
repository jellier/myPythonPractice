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




# with常用来处理文件，你需要获取一个文件句柄，从文件中读取数据，然后关闭文件句柄。

# file = open("/tmp/foo.txt")
# data = file.read()
# file.close()


# 这里有两个问题。一是可能忘记关闭文件句柄；二是文件读取数据发生异常，没有进行任何处理。下面是处理异常的加强版本：

# file = open("/tmp/foo.txt")
# try:
#     data = file.read()
# finally:
#     file.close()


# 虽然这段代码运行良好，但是太冗长了。这时候就是with一展身手的时候了。除了有更优雅的语法，with还可以很好的处理上下文环境产生的异常。下面是with版本的代码：

# with open("/tmp/foo.txt") as file:
#     data = file.read()

# Python对with的处理很聪明。基本思想是with所求值的对象必须有一个__enter__()方法，一个__exit__()方法。
# 紧跟with后面的语句被求值后，返回对象的__enter__()方法被调用，这个方法的返回值将被赋值给as后面的变量。
# 当with后面的代码块全部被执行完之后，将调用前面返回对象的__exit__()方法。

# Python的with语句是提供一个有效的机制，让代码更简练，同时在异常产生时，清理工作更简单。
