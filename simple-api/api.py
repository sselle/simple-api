
from flask import Flask
import json

app = Flask(__name__)

def get_ts():
    response = {
        'time': '2020-05-20T10:45:59+00:00',
        'speed': '123.5',
        'gear': 3,
        'gas-ok': True 
    }
    return json.dumps(response)

def get_assets():
    response = {
        'ID': '123',
        'color': 'green',
        'location': 'nbg',
        'connected': True 
    }
    return json.dumps(response)

@app.route('/', methods=['GET'])
def home():
    print('listening...')
    return "<h1>API Example</h1><p>for timeseries and asset data </p>"

@app.route('/timeseries/', methods=['GET'])
def timeseries():
    return get_ts()

@app.route('/assets/', methods=['GET'])
def assets():
    response = get_assets()
    return response

app.run()
