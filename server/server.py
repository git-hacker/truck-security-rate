from flask import Flask, jsonify, request, abort,url_for,render_template,redirect
from time import time
from pymongo.objectid import ObjectId
from bson.json_util import dumps
from bson.objectid import ObjectId
import pymongo

app = Flask(__name__)

mongo = pymongo.MongoClient('127.0.0.1', 27017)
db = mongo.score

@app.route('/homepage/',methods=['GET'])
def index():
    score = db.score.find({},{'_id':1, 'profle': 1, 'name': 1 , 'master_score':1 } ).sort({"master_score" : 1}).limit(10)
    #result = jsonify(score)
    #print(result)
    return dumps(result, default=json_util.default)

@app.route('/detail/', methods=['GET'])
def detail():
    _id = request.args.get('_id')
    if not _id:
        abort(400)
    detail = db.score.find_one({'_id':ObjectId(_id)},{ 'profle': 1, 'name': 1 , 't_plate':1, 'master_score':1,'avg_safety_score':1,'rest_score':1,'nbr_trip':1,'avg_rest':1,'nbr_violations':1,'nbr_accident':1,'avg_daily_dist':1,'total_dist_drive':1,'nbr_days_drive':1,'truck_age':1,'nbr_truck_maintenance':1,'latest_change_time':1} )
    #result = jsonify(detail)
    #print(result)
    return dumps(result, default=json_util.default)


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
