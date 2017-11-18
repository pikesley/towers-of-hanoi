class Towers:
    def __init__(self, discs):
        self.discs = discs
        self.stacks = [range(self.discs - 1, -1, -1), [], []]
        self.count = 0
        self.binarise()
        self.flip = None

    def binarise(self):
        self.binary = format(self.count, '0%sb' % self.discs)
        return self.binary

    def move(self):
        self.count = self.count + 1
        self.diff()

    def diff(self):
        for i in range(self.discs):
            if self.binary[::-1][i] == '0' and self.binarise()[::-1][i] == '1':
                self.flip = i

    def inspect(self):
        return {
            "stacks": self.stacks,
            "count": self.binary,
            "flip": self.flip
        }
