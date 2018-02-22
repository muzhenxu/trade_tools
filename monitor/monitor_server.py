from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/get_data', methods=['GET', 'POST'])
def get_data():
    upper = request.args.get('u', 1000000)
    lower = request.args.get('l', 0)
    print(upper, lower)
    return json.dumps({'upper':upper, 'lower':lower})

if __name__ == '__main__':
    app.run()
