from indexer import Indexer

class Hanoi(list):
    def __init__(self, count):
        self.count = count
        for i in range(3):
            self.append([])

        for i in range(self.count):
            self[0] = [i] + self[0]

    def move(self, disc):
        pole = 0
        for i in range(self.count):
            try:
                self[i].index(disc) == self.count
                pole = i
            except ValueError:
                pass

        mover = self[pole].pop()
        if len(self[(pole + 1) % 3]) and self[(pole + 1) % 3][-1] < mover:
            self[(pole + 2) % 3].append(mover)
        else:
            self[(pole + 1) % 3].append(mover)

if __name__ == '__main__':
    h = Hanoi(3)
    for index in Indexer(4):
        print h
        h.move(index)

    print h
