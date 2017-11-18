from towers import Towers


towers = Towers(3)

def test_start_state():
    assert towers.inspect() == {
        "stacks": [
            [2, 1, 0],
            [],
            []
        ],
        "count": "000",
        "flip": None
    }

def test_first_move():
    towers.move()
    assert towers.inspect()["count"] == "001"
    #assert towers.inspect()["flip"] == 0

    # assert towers.inspect() == {
    #     "stacks": [
    #         [2, 1],
    #         [0],
    #         []
    #     ],
    #     "count": "001",
    #     "flip": 0
    # }
