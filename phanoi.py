import sys
import time

from microdotphat import clear, set_pixel, show
from towers import Towers

INTERVAL = 0.1


def phat_stacks(towers):
    clear()
    offset = 0
    for stack in towers.stacks:
        count = 0
        for disc in stack:
            shim = int((5 - (disc + 1)) / 2)
            for i in range(disc + 1):
                set_pixel(i + offset + shim, 6 - count, 1)
            count = count + 1
        offset = offset + 8
        show()


if __name__ == '__main__':
    try:
        discs = int(sys.argv[1])
    except IndexError:
        discs = 3
    except ValueError:
        discs = 3
    if discs == 0:
        discs = 3

    while True:
        towers = Towers(discs)
        phat_stacks(towers)
        print towers.binary

        moves = 0
        while not towers.solved():
            time.sleep(INTERVAL)
            towers.move()
            phat_stacks(towers)
            print towers.binary
            moves = moves + 1

        time.sleep(INTERVAL * 3)
