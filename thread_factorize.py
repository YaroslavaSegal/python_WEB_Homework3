import multiprocessing
from multiprocessing import Process
from time import time

num = multiprocessing.cpu_count() # num == 8 on my notebook


def worker(value):
    if value == 0:
        return None
    elif value == 1:
        return value
    else:
        value_lst = []
        for i in range(1, value + 1):
            if value % i == 0:
                value_lst.append(i)
        print(value_lst)


if __name__ == '__main__':
    numbers = [128, 255, 675, 99999, 10651060, 15876342, 17999481, 87545321]
    processes = []

    for el in numbers:
        pr = Process(target=worker, args=(el,))
        processes.append(pr)

    timer = time()
    [pr.start() for pr in processes]
    [pr.join() for pr in processes]
    [pr.close() for pr in processes]
    print(f'Done by {num} processes: {round(time() - timer, 4)}')
