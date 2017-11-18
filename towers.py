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

        stack = 0
        for i in range(3):
            try:
                self.stacks[i].index(self.flip) == self.count
                stack = i
            except ValueError:
                pass

        mover = self.stacks[stack].pop()

        if len(self.stacks[(stack + 1) % 3]) \
                and self.stacks[(stack + 1) % 3][-1] < mover:
            self.stacks[(stack + 2) % 3].append(mover)
        else:
            self.stacks[(stack + 1) % 3].append(mover)

    def diff(self):
        for i in range(self.discs):
            if self.binary[::-1][i] == '0' and self.binarise()[::-1][i] == '1':
                self.flip = i

    def solved(self):
        return all(c == '1' for c in list(self.binary))

    def inspect(self):
        return {
            "stacks": self.stacks,
            "count": self.binary,
            "flip": self.flip
        }

    def pretty_stacks(self):
        s = ''
        for stack in self.stacks:
            s += str(stack)
            s += "\n"
        s += "------"

        return s
