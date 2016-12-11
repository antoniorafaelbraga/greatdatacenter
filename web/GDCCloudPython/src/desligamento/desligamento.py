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

    def desligarCluster(self, status):

        
        
        
        print 'Cluster Desligado'        