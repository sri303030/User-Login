from flask import Flask
from flask import request
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/api/v1/login', methods=['POST'])
def login():
    print request.data
    user = json.loads(request.data, strict=False)['userName']
    pwd = json.loads(request.data,strict=False)['password']

    if user == 'admin' and pwd == 'admin':
        return 'Success'
    else:
        return 'Fail'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8686, debug=True)
