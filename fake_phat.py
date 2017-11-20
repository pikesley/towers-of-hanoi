s = ''
row = 0


def clear():
    global s, row
    s = ''
    row = 0


def set_pixel(j, i, bit):
    global s, row

    if row != i:
        row = i
        s += "\n"

    if (4 - (j % 8)) < 0:
        s += ' '
    else:
        if bit == 0:
            s += '.'
        if bit == 1:
            s += 'o'


def show():
    global s
    print s
