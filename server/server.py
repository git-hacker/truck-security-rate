from flask import Flask, jsonify, request, abort,url_for,render_template,redirect
from time import time
from bson.json_util import dumps
from bson import json_util
from bson.objectid import ObjectId
from pymongo import MongoClient


app = Flask(__name__)

client = MongoClient()
db = client.HackDB01

@app.route('/homepage/',methods=['GET'])
def index():
    result = db.score.find({},{'_id':1, 'profile': 1, 'name': 1 , 'master_score':1 } ).sort([("master_score", -1)]).limit(10)
    #result = jsonify(score)
    #print(result)
    return dumps(result, default=json_util.default)

@app.route('/detail/', methods=['GET'])
def detail():
    id = request.args.get('_id')
    if not id:
        abort(400)
    detail = db.score.find_one({'_id':ObjectId(id)} )
    #result = jsonify(detail)
    #print(result)
    return dumps(detail, default=json_util.default)


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
