import sys
import time

from microdotphat import clear, set_pixel, show
from hanoi import Hanoi

if __name__ == '__main__':
    try:
        count = int(sys.argv[1])
    except IndexError:
        count = 3
    except ValueError:
        count = 3
    if count == 0:
        count = 3

    h = Hanoi(count)
    h.run()
    print h

    for state in h.states:
        clear()
        offset = 0
        for pole in state:
            count = 0
            for disc in pole:
                for i in range(disc + 1):
                    set_pixel(i + offset, 6 - count, 1)
                count = count + 1
            offset = offset + 8
            show()
        time.sleep(0.75)
