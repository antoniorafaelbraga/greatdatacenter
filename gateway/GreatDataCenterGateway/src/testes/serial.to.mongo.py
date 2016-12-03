#!/usr/bin/python
import serialgw
import time
import json
import bson
import collections
from bson.codec_options import CodecOptions
from collections import OrderedDict
from pymongo import MongoClient

while True:

    print "=============================SERIAL========================="
    ser = serialgw.Serial("/dev/ttyUSB0", 9600);
    print "Iniciando"
    ser.flush()
    serialgw = ser.readline().rstrip("\n").rstrip("\r")
    time.sleep(1)
    jsontest = {"temperature": serialgw[16:21], "humidity": serialgw[35:40]}
    print "Leu Json"
    print jsontest
    #time.sleep(1)
    print "============================================================"
    
    print "=============================BD============================="
    #connection = MongoClient('192.168.56.101', 27017) #servidor local
    connection = MongoClient('52.67.30.209', 27017) #servidor remoto
    db = connection['greatDataCenter']
    db.authenticate('gdc', 'gdc')
    collection = db['cluster_room']
    print "Conectou com o MongoDB"
    print "============================================================"

    
    #jsonstr = json.dumps(jsondict) # objeto em string JSON.
    #jsonobj1 = json.loads(jsonstr) # string JSON em objeto.
    cr = db.cluster_room
    post_id = cr.insert_one(jsontest).inserted_id
    print "Salvou o json"