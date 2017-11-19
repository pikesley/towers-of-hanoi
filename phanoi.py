import time
import requests
import json

from towers import Towers

INTERVAL = 0.3
DISCS = 5


def display(towers):
    url = 'http://localhost:5000/lights'
    payload = {"data": towers.phat_matrix()}
    headers = {'content-type': 'application/json'}
    requests.post(url, data=json.dumps(payload), headers=headers)


if __name__ == '__main__':
    while True:
        towers = Towers(DISCS)
        display(towers)
        print towers.binary
        time.sleep(INTERVAL * 3)

        while not towers.solved():
            towers.move()
            display(towers)
            print towers.binary
            time.sleep(INTERVAL)

        time.sleep(INTERVAL * 10)
