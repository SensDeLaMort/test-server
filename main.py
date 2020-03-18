from flask import Flask, request
import json


app = Flask(__name__)


@app.route('/', method=["POST"])
def processing():
    data = json.loads(request.data)
    return data['tag']
