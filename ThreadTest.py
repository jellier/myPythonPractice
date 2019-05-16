# 用多线程并发解决问题

import threading
import time
# 使用current_thread获取当前线程信息
from threading import current_thread

# def myThread(arg1, arg2):
#     print(current_thread().getName(),'start')
#     print('%s %s' %(arg1, arg2))
#     time.sleep(3)
#     print(current_thread().getName(),'stop')
#
#
# for i in range(1 ,6 ,1):
#     # t1 = myThread(i , i+1)
#     t1 = threading.Thread(target= myThread, args=(i , i+1))
#     t1.start()
#
# print(current_thread().getName(),'end')

# 以上代码的问题是当主进程end时，子进程的stop还未打印


# 希望线程同步，即子线程都结束后再让主线程结束
# 定义一个类，继承threading.Thread类
class Mythread(threading.Thread): #参数不可以带括号，因为不是引用
    def run(self):
        print(current_thread().getName(),'start')
        print('run')
        time.sleep(2)
        print(current_thread().getName(),'stop')
for i in range(1, 6, 1):
    t2 = Mythread()
    t2.start()
    t2.join()
# t2.join()

# join方法：阻塞调用线程，直到队列中的所有任务被处理掉。
# join放在for循环外，5个start一起开始，sleep2秒后再一起结束，最后结束主进程
# join放在for循环内，每个子进程开始--结束，sleep2秒后再开始下一个子进程，5个子进程都结束后，最后结束主进程
print(current_thread().getName(),'end')