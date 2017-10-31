from hanoi import Hanoi

class TestHanoi:
    def test_structure(self):
        h = Hanoi(3)
        assert h == [[2, 1, 0], [], []]

    def test_move(self):
        h = Hanoi(3)
        h.move(0)
        assert h == [[2, 1], [0], []]

    def test_wrapping(self):
        h = Hanoi(3)
        h.move(0)
        h.move(0)
        h.move(0)

        assert h == [[2, 1, 0], [], []]

    def test_stacking(self):
        h = Hanoi(3)
        h.move(0)
        h.move(1)

        print h
        assert h == [[2], [0], [1]]
