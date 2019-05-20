# 生产者和消费者问题

# 生产者消费者模式并不是GOF提出的23种设计模式之一，23种设计模式都是建立在面向对象的基础之上的，但其实面向过程的编程中也有很多高效的编程模式，生产者消费者模式便是其中之一，它是我们编程过程中最常用的一种设计模式。

# 下面的例子生产者经过一个随机的时间往队列里添加一个数字，消费者经过一个随机的时间从队列里取出一个数字
# 使用到queue库

from threading import Thread,current_thread
import time
import random
from queue import Queue

workQueue = Queue(5)
# 定义一个生产者类，继承自threading.Thread类
class ProducerThread(Thread):
    def run(self):
        # 提取生产者的线程名称
        name = current_thread().getName()
        # 随机产生一个数字，用于放入队列
        nums = range(100)
        global workQueue
        # for i in range(3):
        while True:
            num = random.choice(nums)
            workQueue.put(num)
            print('生产者 %s 生产了数据 %s' %(name, num))
            t = random.randint(1,3)
            time.sleep(t)
            print('生产者 %s 睡眠了 %s 秒' %(name, t))

class ConsumerTheard(Thread):
    def run(self):
        name = current_thread().getName()
        global workQueue
        # while not queue.empty():
        while True:
            num = workQueue.get()
            # task_done封装好了线程等待和线程同步的方法
            workQueue.task_done()
            print('消费者 %s 消耗了数据 %s' %(name, num))
            t = random.randint(1,5)
            time.sleep(t)
            print('消费者 %s 睡眠了 %s 秒' % (name, t))


p1 = ProducerThread(name = 'p1')
p1.start()
# p2 = ProducerThread(name = 'p2')
# p2.start()
# p3 = ProducerThread(name = 'p3')
# p3.start()
c1 = ConsumerTheard(name = 'c1')
c1.start()
c2 = ConsumerTheard(name = 'c2')
c2.start()

# 当队列满了的时候生产者和消费者都会进入sleep，直到消费者消耗了数据后继续生产
# 如果多线程，可以并发写入和读取，数据多少由队列长队进行控制

# 生产者消费者模式是通过一个容器来解决生产者和消费者的强耦合问题。
# 生产者和消费者彼此之间不直接通讯，而通过阻塞队列来进行通讯，所以生产者生产完数据之后不用等待消费者处理，
# 直接扔给阻塞队列，消费者不找生产者要数据，而是直接从阻塞队列里取，阻塞队列就相当于一个缓冲区，
# 平衡了生产者和消费者的处理能力。