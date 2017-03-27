from flask import Flask
from flask import request
from flask import make_response
import json
import redis
import uuid

app = Flask(__name__)

rclient = redis.Redis(host='localhost', port=6379, db=0)

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/api/v1/login', methods=['POST'])
def login():

    ip = request.headers.get('X-Real-Ip')
    method = request.method
    print "Received " + method + " /api/v1/login request from: " + ip + ", body:" + request.data

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
    record = {
	'user': user,
	'password': pwd,
	'ip': ip,
	'result': result
    }
    rclient.set(uuid.uuid1(), json.dumps(record))
    rclient.save()
    return make_response(json.dumps(rsp), status)

@app.route('/api/v1/users', methods=['GET'])
def getUsers():
    ip = request.headers.get('X-Real-Ip')
    method = request.method
    print "Received " + method + " /api/v1/users request from: " + ip

    keys = rclient.keys()
    values = []
    for key in keys: 
	values.append(rclient.get(key))

    return make_response(str(values), 200)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8686, debug=True)
