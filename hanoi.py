# class Disc:
#     def __init__(self, size):
#         self.size = size
#         self.index = 0
#
#     def move(self):
#         if h[self.index][-1] == self:
#             h[self.index].pop()
#             self.index = (self.index + 1) % 3
#             h[self.index].append(self)
#
# class Pole(list):
#     def __init__(self, members = []):
#         for member in members:
#             self.append(member)
#
#     def display(self):
#         print map(lambda x: x.size, self)

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
                self[i].index(disc)
                pole = i
            except ValueError:
                pass

        self[(pole + 1) % 3].append(self[pole].pop())
