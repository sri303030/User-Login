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

    log()

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
        'ip': request.headers.get('X-Real-Ip'),
        'result': result
    }
    add_record(uuid.uuid1(), json.dumps(record))
    return make_response(json.dumps(rsp), status)

@app.route('/api/v1/users', methods=['GET'])
def getUsers():
    
    log()

    ret = {
        'users': get_all_records()
    }
    return make_response(json.dumps(ret), 200)

def log():
    ip = request.headers.get('X-Real-Ip')
    method = request.method
    url = request.url
    data = request.data
    print "Received " + method + " " + url + " from " + ip + ", body:" + request.data

def add_record(key, value):
    rclient.set(key, value)
    rclient.save()

def get_all_records():
    values = []
    for key in rclient.keys():
        content = json.loads(rclient.get(key))
        user = {
            'user': content['user'],
            'password': content['password'],
            'ip': content['ip'],
            'result': content['result']
        }
        values.append(user)
    return values
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8686, debug=True)
