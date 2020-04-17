from flask import *
import requests
import json
app = Flask(__name__)

@app.route('/data')
def data():
    response = requests.get(f"https://thevirustracker.com/free-api?global=stats")
    data1 = response.json()
    data2 = json.dumps(data1)
    return data2

@app.route('/')
def index():
    response = requests.get(f"https://thevirustracker.com/free-api?global=stats")
    data1 = response.json()
    data2 = json.dumps(data1)
    data  = json.loads(data2)
    keys = list()
    values = list()
    for val in data["results"][0]:
        if not isinstance(data["results"][0][val], dict):
            values.append(data["results"][0][val])
            keys.append(val.replace('_', ' '))
        
    print(values)
    print(keys)
    return render_template('home.html', lables = keys, values = values, )

   