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
    
    def insertJson(self, json):
        cr = self.db.cluster_room
        json_id = cr.insert_one(json).inserted_id
        print 'Salvou o json com id: '+str(json_id)
        
    def salveStatus(self, status):
        cr = self.db.status
        status_id = cr.insert_one(status).inserted_id
        print 'Status salvo com id: '+ str(status_id)
        
    def closeConnection(self):
        self.connection.close()