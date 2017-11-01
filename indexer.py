class Indexer(list):
    def __init__(self, limit):
        self.limit = int('1' * limit, 2)
        self.numbers()
        self.indeces()

    def indeces(self):
        for i in range(self.limit):
            this = self.numbers[i][::-1]
            that = self.numbers[i + 1][::-1]

            for j in range(self.width):
                if this[j] == '0' and that[j] == '1':
                    self.append(j)

    def numbers(self):
        self.numbers = []
        self.width = len(format(self.limit, 'b'))
        for i in range(self.limit + 1):
            self.numbers.append(format(i, '0%sb' % self.width))
