import copy
import sys
from indexer import Indexer


class Hanoi:
    def __init__(self, count):
        self.indexer = Indexer(count)
        self.count = count
        self.poles = []
        for i in range(3):
            self.poles.append([])

        for i in range(self.count):
            self.poles[0] = [i] + self.poles[0]

        self.states = [copy.deepcopy(self.poles)]

    def run(self):
        count = 0
        for index in self.indexer:
            self.move(index)
            count = count + 1

    def move(self, disc):
        pole = 0
        for i in range(3):
            try:
                self.poles[i].index(disc) == self.count
                pole = i
            except ValueError:
                pass

        mover = self.poles[pole].pop()
        if len(self.poles[(pole + 1) % 3]) \
                and self.poles[(pole + 1) % 3][-1] < mover:
            self.poles[(pole + 2) % 3].append(mover)
        else:
            self.poles[(pole + 1) % 3].append(mover)

        self.states.append(copy.deepcopy(self.poles))

    def __str__(self):
        s = ''
        for state in self.states:
            for pole in state:
                s += str(pole)
                s += "\n"
            s += "------\n"

        s += "Total of %d moves to solve for %d discs" % \
            (len(self.states) - 1, self.count)

        return s


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
