import sys
from towers import Towers


if __name__ == "__main__":
    try:
        discs = int(sys.argv[1])
    except IndexError:
        discs = 3
    except ValueError:
        discs = 3
    if discs == 0:
        discs = 3

    towers = Towers(discs)
    print towers.pretty_stacks()

    moves = 0
    while not towers.solved():
        towers.move()
        print towers.pretty_stacks()
        moves = moves + 1

    print "%d moves to solve for %d discs" % (moves, discs)
