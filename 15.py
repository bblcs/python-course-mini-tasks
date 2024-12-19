import threading
import queue
import numpy as np
import sys

CAP = 500
N_CONSUMERS = 1

if len(sys.argv) > 1:
    N_CONSUMERS = int(sys.argv[1])


class Producer(threading.Thread):
    def __init__(self, task_queue, lock):
        threading.Thread.__init__(self)
        self.task_queue = task_queue
        self.lock = lock

    def run(self):
        size = 2
        while size <= CAP:
            with self.lock:
                self.task_queue.put((size, 2, 2))
                size += 1
        for i in range(N_CONSUMERS):
            self.task_queue.put((None, None, None))


class Consumer(threading.Thread):
    def __init__(self, task_queue, lock):
        threading.Thread.__init__(self)
        self.task_queue = task_queue
        self.lock = lock

    def run(self):
        while True:
            size, value, times = self.task_queue.get()
            if size is None:
                break
            A = np.fromfunction(lambda i, j: value ** (i + j), (size, size))
            A = np.linalg.matrix_power(A, times)
            print(f"size: {size} x {size} power: {times} sum: {np.sum(A)}")
            self.task_queue.task_done()


task_queue = queue.Queue()
lock = threading.Lock()

producer = Producer(task_queue, lock)
consumers = [Consumer(task_queue, lock) for _ in range(N_CONSUMERS)]

producer.start()
for consumer in consumers:
    consumer.start()

producer.join()
for consumer in consumers:
    consumer.join()
