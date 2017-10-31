class Disc:
    def __init__(self, size):
        self.size = size
        self.index = 0

    def move(self):
        if h[self.index][-1] == self:
            h[self.index].pop()
            self.index = (self.index + 1) % 3
            h[self.index].append(self)

class Pole(list):
    def __init__(self, members = []):
        for member in members:
            self.append(member)

    def display(self):
        print map(lambda x: x.size, self)

class Hanoi(list):
    def __init__(self, count):
        self.discs = []
        for i in range(count):
            self.discs.append(Disc(i))

        for i in range(3):
            self.append(Pole())

        self[0] = Pole(members = self.discs[:])
        self[0].reverse()

    def display(self):
        for pole in self:
            pole.display()

if __name__ == '__main__':
    h = Hanoi(2)
    h.display()
    print '---'

    h.discs[0].move()
    h.display()
    print '---'

    h.discs[0].move()
    h.display()
    print '---'

    h.discs[0].move()
    h.display()
