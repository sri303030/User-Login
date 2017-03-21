from flask import Flask
from flask import request
from flask import make_response
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/api/v1/login', methods=['POST'])
def login():

    ip = request.headers.get('X-Real-Ip')

    print "Received request from: " + ip + ", body:" + request.data

    user = json.loads(request.data, strict=False)['userName']
    pwd = json.loads(request.data, strict=False)['password']

    if user == 'admin' and pwd == 'admin':
        result = 'Success'
        status = 201
    else:
        result = 'Fail'
        status = 403
    rsp = {
        'user': user,
        'result': result
    }
    return make_response(json.dumps(rsp), status)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8686, debug=True)
