import time
from towers import Towers

INTERVAL = 0.3
DISCS = 5


def display(towers):
    s = ''
    for i in range(7):
        for j in range(45):
            bit = towers.phat_matrix()[i][j]
            if (4 - (j % 8)) < 0:
                s += ' '
            else:
                if bit == 0:
                    s += '.'
                if bit == 1:
                    s += 'o'
            s += ' '

        s += "\n"
    print s


if __name__ == '__main__':
    while True:
        towers = Towers(DISCS)
        display(towers)
        time.sleep(INTERVAL)

        while not towers.solved():
            towers.move()
            display(towers)
            time.sleep(INTERVAL)

        time.sleep(INTERVAL)
