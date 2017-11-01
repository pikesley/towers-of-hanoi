import copy
from indexer import Indexer

class Hanoi:
    def __init__(self, count):
        self.indexer = Indexer(3)
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
        for i in range(self.count):
            try:
                self.poles[i].index(disc) == self.count
                pole = i
            except ValueError:
                pass

        mover = self.poles[pole].pop()
        if len(self.poles[(pole + 1) % 3]) and self.poles[(pole + 1) % 3][-1] < mover:
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

        return s

if __name__ == '__main__':
    h = Hanoi(2)
    h.run()
    print h
