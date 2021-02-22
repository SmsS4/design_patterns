import time
import multiprocessing


def worker(x):
    print(f"Worker-{x} started")
    time.sleep(2)
    print(f"Worker-{x} finished")


if __name__ == '__main__':
    with multiprocessing.Pool(4) as pool:
        pool.map(worker, [i for i in range(20)])

