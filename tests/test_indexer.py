from indexer import Indexer


class TestCounter:
    def test_indexes_for_2(self):
        assert Indexer(2) == [0, 1, 0]

    def test_indexes_for_3(self):
        assert Indexer(3) == [
            0, 1, 0, 2,
            0, 1, 0
        ]

    def test_indexes_for_4(self):
        assert Indexer(4) == [
            0, 1, 0, 2,
            0, 1, 0, 3,
            0, 1, 0, 2,
            0, 1, 0
        ]

    def test_indexes_for_5(self):
        assert Indexer(5) == [
            0, 1, 0, 2,
            0, 1, 0, 3,
            0, 1, 0, 2,
            0, 1, 0, 4,
            0, 1, 0, 2,
            0, 1, 0, 3,
            0, 1, 0, 2,
            0, 1, 0
        ]

    def test_list(self):
        i = Indexer(2)
        assert i.numbers == ['00', '01', '10', '11']

        j = Indexer(3)
        assert j.numbers == [
            '000', '001', '010', '011',
            '100', '101', '110', '111'
        ]
