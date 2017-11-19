from flask import Flask, request
import json
from microdotphat import clear, set_pixel, show

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello Foo!"


@app.route("/lights", methods=['POST'])
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
    app.run(host='0.0.0.0')
