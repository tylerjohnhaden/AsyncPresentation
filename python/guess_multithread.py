import json
import threading

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


def worker(queue):
    while True:
        try:
            g = next(queue)
            print('guessing .. {0}'.format(g))
            if attempt(g):
                return
        except StopIteration:
            return


if __name__ == '__main__':
    shared_guess_queue = guess_queue()
    threads = list(threading.Thread(target=worker, args=(shared_guess_queue,)) for _ in range(512))

    for t in threads:
        t.start()
