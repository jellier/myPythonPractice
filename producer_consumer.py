# 生产者和消费者问题
# 下面的例子生产者经过一个随机的时间往队列里添加一个数字，消费者经过一个随机的时间从队列里取出一个数字
# 使用到queue库

from threading import Thread,current_thread
import time
import random
from queue import Queue

queue = Queue(5)
# 定义一个生产者类，继承自threading.Thread类
class ProducerThread(Thread):
    def run(self):
        name = current_thread().getName()
        nums = range(100)
        global queue
        while True:
            num = random.choice(nums)
            queue.put(num)
            print('生产者 %s 生产了数据 %s' %(name, num))
            t = random.randint(1,3)
            time.sleep(t)
            print('生产者 %s 睡眠了 %s 秒' %(name, t))

class ConsumerTheard(Thread):
    def run(self):
        name = current_thread().getName()
        global queue
        while True:
            num = queue.get()
            queue.task_done()
            print('消费者 %s 消耗了数据 %s' %(name, num))
            t = random.randint(1,5)
            time.sleep(t)
            print('消费者 %s 睡眠了 %s 秒' % (name, t))


p1 = ProducerThread(name = 'p1')
p1.start()
p2 = ProducerThread(name = 'p2')
p2.start()
p3 = ProducerThread(name = 'p3')
p3.start()
c1 = ConsumerTheard(name = 'c1')
c1.start()
c2 = ConsumerTheard(name = 'c2')
c2.start()

# 当队列满了的时候生产者和消费者都会进入sleep，直到消费者消耗了数据后继续生产
# 如果多线程，可以并发写入和读取，数据多少由队列长队进行控制