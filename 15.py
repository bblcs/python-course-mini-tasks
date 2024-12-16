import threading
import queue
import numpy as np

CAP = 500
N_CONSUMERS = 4


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


def main():
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


if __name__ == "__main__":
    main()


# benchmarking:
# $ hyperfine 'python 15.py' './python313_nogil 15.py'
# Benchmark 1: python 15.py
#   Time (mean ± σ):     16.758 s ±  1.514 s    [User: 35.490 s, System: 0.594 s]
#   Range (min … max):   15.461 s … 19.976 s    10 runs

# Benchmark 2: ./python313_nogil 15.py
#   Time (mean ± σ):     11.918 s ±  0.633 s    [User: 34.283 s, System: 0.316 s]
#   Range (min … max):   10.919 s … 12.620 s    10 runs

# Summary
#   ./python313_nogil 15.py ran
#     1.41 ± 0.15 times faster than python 15.py
