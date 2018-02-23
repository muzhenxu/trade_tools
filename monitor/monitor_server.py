from flask import Flask, request
import json

import itchat

app = Flask(__name__)

@app.route('/get_data', methods=['GET', 'POST'])
def get_data():
    upper = request.args.get('u', 1000000)
    lower = request.args.get('l', 0)
    print(upper, lower)
    return json.dumps({'upper':upper, 'lower':lower})

@app.route('/send_alarm', methods=['POST'])
def send_alarm():
    data = request.json
    itchat.send_msg(msg=str(data), toUserName=None)
    return json.dumps({'code':0, 'msg':'succ'})

if __name__ == '__main__':
    itchat.auto_login(enableCmdQR=2)
    app.run(host='0.0.0.0', port=5000, debug=True)
