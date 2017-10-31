import json
import multiprocessing

import requests


def attempt(guess):
    try:
        data = json.loads(requests.get('http://localhost:7777/{0}'.format(guess)).text)
        if 'success' in data:
            print(data)
            return True
    except Exception as e:
        print(e)
        pass
    return False


def guess_queue():
    for i in range(1 + (2 ** 21)):
        yield i


def worker(a, b):
    for i in range(a, b):
        print('guessing .. {0}'.format(i))
        if attempt(i):
            return


if __name__ == '__main__':
    n = 40
    workload = int((1 + (2 ** 21)) / n)
    pool = [multiprocessing.Process(target=worker, args=(i, i + workload)) for i in range(0, 1 + (2 ** 21), workload)]

    for p in pool:
        p.start()
