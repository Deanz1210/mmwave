from flask import Flask, render_template
import json

app = Flask(__name__, static_folder='static')

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/data')
def get_data():
    # with open('C:/Users/user/PycharmProjects/mmWave-Read-Data/static/data/testdata2.json', 'r') as f:
    with open('C:/Users/user/PycharmProjects/mmWave-Read-Data/static/data/output.json', 'r') as f:
        data = json.load(f)
    return render_template('data.html', data=data)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9997, debug=True)
