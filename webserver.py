from flask import Flask, request
import json
import os

app = Flask(__name__)

RASPI = os.uname()[1] == 'raspberrypi'

if RASPI:
    from microdotphat import clear, set_pixel, show
else:
    from fake_phat import clear, set_pixel, show


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
