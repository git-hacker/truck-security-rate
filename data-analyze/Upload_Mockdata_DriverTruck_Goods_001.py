# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 11:16:22 2018

@author: pierr
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 22:31:27 2018

@author: pierr
"""
# Set working directory
import os
path = 'C:/Users/pierr/Documents/GitHub/truck-security-rate/data-analyze/MockDateTemplate'
os.chdir(path)

# Import data
import pandas as pd
df_d = pd.read_csv("MOCK_DATA.csv")
df_t = pd.read_csv("MOCK_DATA_truck.csv")
df_g = pd.read_csv("MOCK_DATA_goods.csv")
zipcode = pd.read_csv("zipcodeVF.csv")
avatar = pd.read_csv("avatar.csv")

# combine driver and trucks
df_dt = pd.concat([df_d.reset_index(drop=True), df_t], axis=1)

#Step 2: Create sample data for driver and truck
from random import randint
from datetime import datetime
from datetime import timedelta

# driver data
d_name = df_dt.d_name
d_avatar = avatar['0'].values.tolist()
d_phone_nb = df_dt.d_phone_nb
d_license = df_dt.d_license.astype(str)
d_idcard = df_dt.d_idcard
d_gender = df_dt.gender
d_birthdate =  pd.to_datetime(df_dt.d_birthdate)
d_birthplace = zipcode['0'].values.tolist()

# truck data
t_VIN = df_dt.t_VIN
t_plate = df_dt.t_plate
t_enginetype = ["diesel", "gasoline", "electric", "hybrid"] 
t_make = df_dt.t_make
t_model = df_dt.t_model
t_num_engine = df_dt.t_num_engine
t_regdate =  pd.to_datetime(df_dt.t_regdate)
t_issuedate =  pd.to_datetime(df_dt.t_issuedate)
t_maxload = df_dt.t_maxload.astype(str)
t_width = df_dt.t_width.astype(str)
t_length = df_dt.t_length.astype(str)
t_heigth = df_dt.t_heigth.astype(str)
t_tyrechangedate =  pd.to_datetime(df_dt.t_tyrechangedate)
t_engineoilchangedate =  pd.to_datetime(df_dt.t_engineoilchangedate)

# goods data
g_pickdate = pd.to_datetime(df_g.g_pickdate)
g_pickzipcode = zipcode['0'].values.tolist()
g_delivzipcode = zipcode['0'].values.tolist()
g_dist = df_g.g_dist
g_weight = df_g.g_weight.astype(str)
g_movement = df_g.g_rest.astype(str)
g_num_violations = ['speed', 'line', 'emergency', 'drug', 'CLEAR']
g_accident = ['sleep', 'alcohol', 'external', 'CLEAR']
g_incident =  ['tyre', 'motor', 'structure', 'CLEAR']

# Set database connection
from pymongo import MongoClient
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient()
db = client.HackDB01

db.DriversTrucks.delete_many({})
db.Goods.delete_many({})

# set number of driver/truck to add to DB
n_dt = 1000
# set number of trips for each driver
n_g = 300

for x in range(1, n_dt):
    # Create fake data for driver and truck and loop
    data_dt = {
        'd_name' : d_name[randint(0, (len(d_name)-1))],
        'd_avatar': d_avatar[randint(0, len(d_avatar)-1)],
        'd_phone_nb' : d_phone_nb[randint(0, (len(d_phone_nb)-1))],
        'd_license': d_license[randint(0, (len(d_license)-1))],
        'd_id_card': d_idcard[randint(0, (len(d_idcard)-1))],
        'd_gender': d_gender[randint(0, len(d_gender)-1)],
        'd_birthdate': d_birthdate[randint(0, len(d_birthdate)-1)],
        'd_birthplace': d_birthplace[randint(0, len(d_birthplace)-1)],
        't_VIN' : t_VIN[randint(0, (len(t_VIN)-1))],
        't_plate' : t_plate[randint(0, (len(t_plate)-1))],
        't_enginetype': t_enginetype[randint(0, (len(t_enginetype)-1))],
        't_make': t_make[randint(0, (len(t_make)-1))],
        't_model': t_model[randint(0, len(t_model)-1)],
        't_num_engine': t_num_engine[randint(0, len(t_num_engine)-1)],
        't_regdate': t_regdate[randint(0, len(t_regdate)-1)],
        't_issuedate': t_issuedate[randint(0, len(t_issuedate)-1)],
        't_maxload': t_maxload[randint(0, len(t_maxload)-1)],
        't_width': t_width[randint(0, len(t_width)-1)],
        't_length': t_length[randint(0, len(t_length)-1)],
        't_heigth': t_heigth[randint(0, len(t_heigth)-1)],
        't_tyrechangedate': t_tyrechangedate[randint(0, len(t_tyrechangedate)-1)],
        't_engineoilchangedate': t_engineoilchangedate[randint(0, len(t_engineoilchangedate)-1)]
    }
    
    #Step 3: Insert business object directly into MongoDB via isnert_one
    result = db.DriversTrucks.insert_one(data_dt)
    
    #Step 4: Print to the console the ObjectID of the new document
    print('Created driver profile {0} as {1}'.format(x, result.inserted_id))
    
    res = str(result.inserted_id)
    # Add trip data for a driver
    for y in range(1, n_g):
        data_g = {
                'g_pickdate' : g_pickdate[y],
                'g_pickzipcode' : g_pickzipcode[randint(0, (len(g_pickzipcode)-1))],
                'g_delivdate' : g_pickdate[y] + timedelta(days = randint(0, 8)),
                'g_dist': g_dist[randint(0, (len(g_dist)-1))],
                'g_weight': g_weight[randint(0, (len(g_weight)-1))],
                'g_movement': g_movement[randint(0, len(g_movement)-1)],
                'g_num_violations': g_num_violations[randint(0, len(g_num_violations)-1)],
                'g_accident': g_accident[randint(0, len(g_accident)-1)],
                'g_incident': g_incident[randint(0, len(g_incident)-1)],
                't_id': res
    }
    
        #Step 3: Insert business object directly into MongoDB via isnert_one
        result = db.Goods.insert_one(data_g)
 
# Disconnect from DB
client.close()
