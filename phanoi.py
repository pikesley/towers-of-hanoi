import sys
import time

from microdotphat import clear, set_pixel, write_string, show
from towers import Towers

INTERVAL = 0.3


def phat_stacks(towers):
    clear()

    bit_offset = 0
    toggle = 5
    for bit in list(towers.binary):
       # write_string(bit, offset_x=24 + bit_offset)
        digit(bit, 27 + bit_offset)
        bit_offset = bit_offset + toggle
        if toggle == 3:
            toggle = 5
        else:
            toggle = 3
            

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

def digit(value, offset):
    for i in range(3, 6):
        if int(value) == 0:
            set_pixel(offset, i, 1)
        set_pixel(offset + 1, i, 1)

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
        time.sleep(INTERVAL * 3)

        moves = 0
        while not towers.solved():
            towers.move()
            phat_stacks(towers)
            print towers.binary
            moves = moves + 1
            time.sleep(INTERVAL)

        time.sleep(INTERVAL * 10)
