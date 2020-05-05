from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/foo', methods=['POST']) 
def getData():
    print('Getting data')
    data = request.json
    with open("data.json", "a") as datafile:
        json.dump(data, datafile)
        datafile.write('\n')
    return jsonify(data)

@app.route('/fooread', methods=['GET'])
def readData():
    print('Reading data')
    for line in open('data.json', 'r'):
        data = json.loads(line)
        print(data["userId"])
    return 'DONE!'
