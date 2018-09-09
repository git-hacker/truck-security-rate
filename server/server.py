from flask import Flask, request, abort,Response
from bson.json_util import dumps
from bson import json_util
from bson.objectid import ObjectId
from pymongo import MongoClient
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

client = MongoClient()
db = client.HackDB01

@app.route('/homepage/',methods=['GET'])
def index():
    result = db.score.find({},{'_id':1, 'd_avatar': 1, 'd_name': 1 , 'master_score':1, 'truck_score':1 } ).limit(10)
    #result = jsonify(score)
    #print(result)
    r = Response(dumps(result, default=json_util.default), status=200, mimetype="application/xml")
    r.headers["Content-type"]="appication/json; charset=urf-8"
    return r 

@app.route('/detail/', methods=['GET'])
def detail():
    id = request.args.get('_id')
    if not id:
        abort(400)
    detail = db.score.find_one({'_id':ObjectId(id)} )
    #result = jsonify(detail)
    #print(result)
    r = Response(dumps(detail, default=json_util.default), status=200, mimetype="application/xml")
    r.headers["Content-type"]="appication/json; charset=urf-8"
    return r


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

