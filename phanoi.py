import sys
import time

from microdotphat import clear, set_pixel, write_string, show
from towers import Towers

INTERVAL = 0.5


def phat_stacks(towers):
    clear()

    bit_offset = 0
    for bit in list(towers.binary):
        write_string(bit, offset_x=24 + bit_offset)
        bit_offset = bit_offset + 8

    offset = 0
    for stack in towers.stacks:
        count = 0
        for disc in stack:
            shim = int((5 - (disc * 2 + 1)) / 2)
            for i in range(disc * 2 + 1):
                set_pixel(i + offset + shim, 6 - count, 1)
                set_pixel(i + offset + shim, 5 - count, 1)
            count = count + 2
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
