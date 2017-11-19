from flask import Flask, request
import json
import os

app = Flask(__name__)

RASPI = os.uname()[1] == 'raspberrypi'
if RASPI:
    from microdotphat import clear, set_pixel, show

@app.route("/lights", methods=['PATCH'])
def lights():
    data = json.loads(request.data)['data']
    if RASPI:
        clear()
    else:
        s = ''

    for i in range(7):
        for j in range(45):
            if RASPI:
                try:
                    set_pixel(j, i, data[i][j])
                except IndexError:
                    pass
            else:
                bit = data[i][j]
                if (4 - (j % 8)) < 0:
                    s += ' '
                else:
                    if bit == 0:
                        s += '.'
                    if bit == 1:
                        s += 'o'
        s += "\n"

    if RASPI:
        show()
    else:
        print s

    return json.dumps({
            'success': True
        }
        ), 200, {
            'ContentType': 'application/json'
        }


if __name__ == "__main__":
    app.run()
