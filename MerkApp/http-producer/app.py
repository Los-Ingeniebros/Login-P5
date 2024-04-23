import json

from flask import Flask, request
from flask_cors import CORS, cross_origin
from random import randint

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

names = ["John", "Matthew", "James", "Brandon", "Tom", "Edward", "Rob", "Patrick", "Josh", "Brock"]
last_names = ["Johnson", "Richardson", "Brown", "Gates", "Robertson", "Greyson", "Wayne", "Mosby", "Purdy"]

def get_random_name():
    return [names[randint(0, len(names)-1)], last_names[randint(0, len(last_names)-1)]]


@app.route('/simulator')
@cross_origin()
def simulate():
    name, last = get_random_name()
    d = {
        "name":name,
        "last_name":last
    }
    return json.dumps(d)

@app.route('/add_name', methods=['POST'])
def add_name():
    name = request.json.get("name", None)
    lastName = request.json.get("last_name", None)
    if name == '' or lastName == '':
        return json.dumps({'error':'Missing parameter'})
    names.append(name)
    last_names.append(lastName)
    return json.dumps({'ok': 'Name added'})

if __name__ == '__main__':
    app.run()
