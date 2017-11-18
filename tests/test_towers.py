from towers import Towers


towers = Towers(3)


def test_zero_state():
    assert towers.inspect() == {
        "stacks": [[2, 1, 0], [], []],
        "count": "000",
        "flip": None
    }


def test_first_state():
    towers.move()
    assert towers.inspect() == {
        "stacks": [[2, 1], [0], []],
        "count": "001",
        "flip": 0
    }


def test_second_state():
    towers.move()
    assert towers.inspect() == {
        "stacks": [[2], [0], [1]],
        "count": "010",
        "flip": 1
    }


def test_third_state():
    towers.move()
    assert towers.inspect() == {
        "stacks": [[2], [], [1, 0]],
        "count": "011",
        "flip": 0
    }


def test_fourth_state():
    towers.move()
    assert towers.inspect() == {
        "stacks": [[], [2], [1, 0]],
        "count": "100",
        "flip": 2
    }


def test_fifth_state():
    towers.move()
    assert towers.inspect() == {
        "stacks": [[0], [2], [1]],
        "count": "101",
        "flip": 0
    }


def test_sixth_state():
    towers.move()
    assert towers.inspect() == {
        "stacks": [[0], [2, 1], []],
        "count": "110",
        "flip": 1
    }


def test_seventh_state():
    towers.move()
    assert towers.inspect() == {
        "stacks": [[], [2, 1, 0], []],
        "count": "111",
        "flip": 0
    }


def test_kosher_game():
    """Ensure that discs in a stack are always in ascending size"""
    towers = Towers(12)

    while not towers.solved():
        towers.move()
        for stack in towers.stacks:
            assert sorted(stack, reverse=True) == stack
