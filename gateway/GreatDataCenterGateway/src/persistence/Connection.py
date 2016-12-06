'''
Created on 21 de nov de 2016

@author: rafaelbraga
'''
from pymongo import MongoClient

''' Classe que conecta com o banco de dados '''
class Connection(object):

    ''' Constructor '''
    def __init__(self, server, port):
        connection = MongoClient(server, port) 
        db = connection['greatDataCenter']
        db.authenticate('gdc', 'gdc')
        
        self.connection = connection
        self.db = db
        print "Conectou com o banco de dados"
    
    def insertJsonSensors(self, json):
        id_sensor = json['id']
        if id_sensor == 1:
            cr = self.db.sensor1
            json_id = cr.insert_one(json).inserted_id
        elif id_sensor == 2:
            cr = self.db.sensor2
            json_id = cr.insert_one(json).inserted_id
        elif id_sensor == 3:
            cr = self.db.sensor3
            json_id = cr.insert_one(json).inserted_id
        
        print 'Salvou o json com id: '+str(json_id)
    
    # persistindo dados do sensor 1
    def getSensor1(self):
        sensor1 = self.db.sensor1
        json_sensor1 = sensor1.find().sort("$natural", -1).limit(1)
        return json_sensor1

    # persistindo dados do sensor 2
    def getSensor2(self):
        sensor2 = self.db.sensor2
        json_sensor2 = sensor2.find().sort("$natural", -1).limit(1)
        return json_sensor2
    
    # persistindo dados do sensor 3
    def getSensor3(self):
        sensor3 = self.db.sensor3
        json_sensor3 = sensor3.find().sort("$natural", -1).limit(1)
        return json_sensor3
    
    def getStatusGDC(self):
        cr = self.db.cluster_room
        status_sistema = cr.find().sort("$natural", -1).limit(1)
        return status_sistema
        
        
    def setStatus(self, status):
        cr = self.db.cluster_room
        status_id = cr.insert_one(status).inserted_id
        print 'Status salvo com id: '+ str(status_id)
        
    def closeConnection(self):
        self.connection.close()