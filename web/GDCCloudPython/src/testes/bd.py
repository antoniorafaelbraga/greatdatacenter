#!/usr/bin/python
import serialgw
import datetime
import json
from pymongo import MongoClient

while True:

    print "=============================SERIAL========================="
    ser = serialgw.SerialGw("/dev/ttyUSB0", 9600);
    print "Iniciando"
    ser.flush()
    json = ser.readline().rstrip("\n").rstrip("\r")
    jsontest = {"temperature": json[16:21], "humidity": json[35:40], "date": datetime.datetime.utcnow()}
    print jsontest  
    print "Leu Json"
    print "============================================================"


    print "=============================BD============================="
    #connection = MongoClient('192.168.56.101', 27017) #servidor local
    connection = MongoClient('52.67.30.209', 27017) #servidor remoto
    db = connection['greatDataCenter']
    db.authenticate('gdc', 'gdc')
    collection = db['cluster_room']
    print "Conectou com o MongoDB"
    
    cr = db.cluster_room
    post_id = cr.insert_one(jsontest).inserted_id
    print "Salvou o json"