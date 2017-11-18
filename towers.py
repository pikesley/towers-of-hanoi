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

        self.source = self.locate_mover()
        self.mover = self.stacks[self.source].pop()

        self.stacks[self.locate_sink()].append(self.mover)

    def locate_mover(self):
        for i in range(3):
            try:
                self.stacks[i].index(self.flip) == self.count
                return i
            except ValueError:
                pass

    def locate_sink(self):
        if len(self.stacks[(self.source + 1) % 3]) \
                and self.stacks[(self.source + 1) % 3][-1] < self.mover:
            return (self.source + 2) % 3
        else:
            return (self.source + 1) % 3

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

    def phat_matrix(self):
        matrix = []
        for i in range(7):
            matrix.append([0] * 45)

        bit_offset = 0
        toggle = 5
        for bit in list(self.binary):
            self.little_digit(bit, matrix, 27 + bit_offset)
            bit_offset = bit_offset + toggle
            if toggle == 3:
                toggle = 5
            else:
                toggle = 3

        offset = 0
        for stack in self.stacks:
            count = 0
            for disc in stack:
                shim = int((5 - (disc + 1)) / 2)
                for i in range(disc + 1):
                    matrix[6 - count][i + offset + shim] = 1
                count = count + 1
            offset = offset + 8
        return matrix

    def little_digit(self, value, matrix, offset):
        for i in range(3, 6):
            if int(value) == 0:
                matrix[i][offset] = 1
            matrix[i][offset + 1] = 1

    def __str__(self):
        return self.pretty_stacks()


if __name__ == "__main__":
    import sys
    try:
        discs = int(sys.argv[1])
    except IndexError:
        discs = 3
    except ValueError:
        discs = 3
    if discs == 0:
        discs = 3

    towers = Towers(discs)
    print towers

    moves = 0
    while not towers.solved():
        towers.move()
        print towers
        moves = moves + 1

    print "%d moves to solve for %d discs" % (moves, discs)
