from hanoi import Hanoi

class TestHanoi:
    def test_structure(self):
        h = Hanoi(3)
        assert h.states[0] == [[2, 1, 0], [], []]

    def test_move(self):
        h = Hanoi(3)
        h.move(0)
        assert h.states[1] == [[2, 1], [0], []]

    def test_wrapping(self):
        h = Hanoi(3)
        h.move(0)
        h.move(0)
        h.move(0)
        assert h.states[3] == [[2, 1, 0], [], []]

    def test_stacking(self):
        h = Hanoi(3)
        h.move(0)
        h.move(1)
        assert h.states[2] == [[2], [0], [1]]

    def test_kosher_game(self):
        h = Hanoi(6)
        h.run()
        for state in h.states:
            for pole in state:
                assert sorted(pole, reverse = True) == pole
