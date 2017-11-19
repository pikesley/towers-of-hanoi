from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/lights", methods=['PATCH'])
def lights():
    data = json.loads(request.data)['data']
    s = ''
    for i in range(7):
        for j in range(45):
            bit = data[i][j]
            if (4 - (j % 8)) < 0:
                s += ' '
            else:
                if bit == 0:
                    s += '.'
                if bit == 1:
                    s += 'o'

        s += "\n"
    print s

    return json.dumps({
            'success': True
        }
        ), 200, {
            'ContentType': 'application/json'
        }


if __name__ == "__main__":
    app.run()
