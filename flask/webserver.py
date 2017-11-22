import markdown
from flask import Flask
from flask import request
from flask import render_template
from flask import Markup
import json
import os

app = Flask(__name__)

RASPI = os.uname()[1] == 'raspberrypi'

if RASPI:
    from microdotphat import clear, show, set_pixel, set_decimal
else:
    from fake_phat import clear, set_pixel, show

@app.route("/")
def index():
  content = open('flask/README.md', 'r').read()
  content = Markup(markdown.markdown(content))
  return render_template('index.html', **locals())

@app.route("/lights", methods=['PATCH'])
def lights():
    try:
        matrix = json.loads(request.data)['matrix']
    except KeyError:
        matrix = [[]]

    try:
        decimals = json.loads(request.data)['decimals']
    except KeyError:
        decimals = []

    clear()

    for i in range(7):
        for j in range(45):
            try:
                set_pixel(j, i, matrix[i][j])
            except IndexError:
                pass
    
    for decimal in decimals:
        set_decimal(decimal, 1)

    show()

    return json.dumps({
            'success': True
        }
        ), 200, {
            'ContentType': 'application/json'
        }


if __name__ == "__main__":
    app.run(host='0.0.0.0')
