from flask import Flask, request
import json
import os

app = Flask(__name__)

RASPI = os.uname()[1] == 'raspberrypi'
s = ''
row = 0

if RASPI:
    from microdotphat import clear, set_pixel, show
else:
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


@app.route("/lights", methods=['PATCH'])
def lights():
    data = json.loads(request.data)['data']
    clear()

    for i in range(7):
        for j in range(45):
            try:
                set_pixel(j, i, data[i][j])
            except IndexError:
                pass

    show()

    return json.dumps({
            'success': True
        }
        ), 200, {
            'ContentType': 'application/json'
        }


if __name__ == "__main__":
    app.run()
