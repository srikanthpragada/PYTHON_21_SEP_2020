from threading import Thread
import threading


class PrintThread(Thread):
    def run(self):
        for i in range(1, 11):
            print(i)


t = PrintThread()
t.start()
print('Current thread :', threading.main_thread().name)
for n in range(1, 11):
    print(n)
