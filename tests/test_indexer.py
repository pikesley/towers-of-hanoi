from indexer import Indexer

class TestCounter:
    def test_indexes_for_4(self):
        assert Indexer(3) == [0, 1, 0]

    def test_indexes_for_7(self):
        assert Indexer(7) == [
            0, 1, 0, 2,
            0, 1, 0
        ]

    def test_indexes_for_15(self):
        assert Indexer(15) == [
            0, 1, 0, 2,
            0, 1, 0, 3,
            0, 1, 0, 2,
            0, 1, 0
        ]

    def test_indexes_for_31(self):
        assert Indexer(31) == [
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
        i = Indexer(3)
        assert i.numbers == ['00', '01', '10', '11']

        j = Indexer(7)
        assert j.numbers == [
            '000', '001', '010', '011',
            '100', '101', '110', '111'
        ]
