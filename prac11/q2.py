from threading import *

class MyThread1(Thread):
    def run(self):
        for i in range(100):
            print("thread-1")

class MyThread2(Thread):
    def run(self):
        for i in range(100):
            print("thread-2")


t1 = MyThread1()
t2 = MyThread2()

t1.start()
t2.start()
# t1.join()
# t2.join()

