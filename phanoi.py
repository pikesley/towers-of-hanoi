import sys
import time

from microdotphat import clear, set_pixel, show
from towers import Towers

INTERVAL = 0.3
DISCS = 5

def display(towers):
    clear()
    for i in range(7):
        for j in range(45):
            set_pixel(j, i, towers.phat_matrix()[i][j])

    show()
        

if __name__ == '__main__':
    while True:
        towers = Towers(DISCS)
        display(towers)
        print towers.binary
        time.sleep(INTERVAL * 3)

        moves = 0
        while not towers.solved():
            towers.move()
            display(towers)
            print towers.binary
            moves = moves + 1
            time.sleep(INTERVAL)

        time.sleep(INTERVAL * 10)
