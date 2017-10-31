import json

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


if __name__ == '__main__':
    for i in range(1 + (2 ** 21)):
        print('guessing .. {0}'.format(i))
        if attempt(i):
            break
