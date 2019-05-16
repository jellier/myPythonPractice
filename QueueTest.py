# queue库的使用
import threading
import queue

# Queue是python标准库中的线程安全的队列（FIFO）实现
# queue.Queue()提供了一个适用于多线程编程的先进先出（FIFO）的数据结构，即队列，用来在生产者和消费者线程之间的信息传递

# class queue.Queue(maxsize=0)
# FIFO即First in First Out,先进先出。Queue提供了一个基本的FIFO容器，使用方法很简单,maxsize是个整数，指明了队列中能存放的数据个数的上限。
# 一旦达到上限，插入会导致阻塞，直到队列中的数据被消费掉。如果maxsize小于或者等于0，队列大小没有限制。
# 如下面的例子，依次将1\2\3放进队列，get时也是按照1、2、3的顺序读取
q = queue.Queue()
q.put(1)
q.put(2)
q.put(3)
print(q.get())  # 1
print(q.get())  # 2
print(q.get())  # 3

q1 = queue.Queue()
for i in range(1, 6):
    q1.put(i)
while not q1.empty():
    print(q1.get(), 'for FIFO')

# LIFO队列:class queue.LifoQueue(maxsize=0)
# LIFO即Last in First Out,后进先出

q2 = queue.LifoQueue()

for i in range(1, 5):
    q2.put(i)

while not q2.empty():
    print(q2.get(), 'for LIFO')


# 优先级队列：class queue.PriorityQueue(maxsize=0)

class Job(object):
    def __init__(self, priority, description):
        self.priority = priority
        self.description = description
        print('Job:', description)
        return

    def __cmp__(self, other):
        return cmp(self.priority, other.priority)


q3 = queue.PriorityQueue()

q3.put(Job(3, 'level 3 job'))
q3.put(Job(10, 'level 10 job'))
# q3.put(Job(1, 'level 1 job'))


def process_job(q3):
    while True:
        next_job = q3.get()
        print('for:', next_job.description)
        q3.task_done()


workers = [
    threading.Thread(
        target=process_job, args=(
            q3,)), threading.Thread(
                target=process_job, args=(
                    q3,))]

for w in workers:
    w.setDaemon(True)
    w.start()

q3.join()


# 一些常用方法
# task_done():
# 意味着之前入队的一个任务已经完成。由队列的消费者线程调用。每一个get()调用得到一个任务，接下来的task_done()调用告诉队列该任务已经处理完毕。
# 如果当前一个join()正在阻塞，它将在队列中的所有任务都处理完时恢复执行（即每一个由put()调用入队的任务都有一个对应的task_done()调用）。
#
# join():
# 阻塞调用线程，直到队列中的所有任务被处理掉。
# 只要有数据被加入队列，未完成的任务数就会增加。当消费者线程调用task_done()（意味着有消费者取得任务并完成任务），未完成的任务数就会减少。当未完成的任务数降到0，join()解除阻塞。
#
# put(item[, block[, timeout]]):
# 将item放入队列中。
# 如果可选的参数block为True且timeout为空对象（默认的情况，阻塞调用，无超时）。
# 如果timeout是个正整数，阻塞调用进程最多timeout秒，如果一直无空空间可用，抛出Full异常（带超时的阻塞调用）。
# 如果block为False，如果有空闲空间可用将数据放入队列，否则立即抛出Full异常
# 其非阻塞版本为put_nowait等同于put(item, False)
#
# get([block[, timeout]]):
# 从队列中移除并返回一个数据。block跟timeout参数同put方法
# 其非阻塞方法为｀get_nowait()｀相当与get(False)
#
# empty():
# 如果队列为空，返回True,反之返回False
