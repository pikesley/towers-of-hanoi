class Towers:
    def __init__(self, discs):
        self.discs = discs
        self.stacks = [range(self.discs - 1, -1, -1), [], []]
        self.count = 0
        self.binary = self.binarise(self.count)
        self.flip = None

    def binarise(self, integer):
        return format(integer, '0%sb' % self.discs)

    def move(self):
        self.count = self.count + 1
        self.binary = self.binarise(self.count)

    def inspect(self):
        return {
            "stacks": self.stacks,
            "count": self.binary,
            "flip": self.flip
        }
