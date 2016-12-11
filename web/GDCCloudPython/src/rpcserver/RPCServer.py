'''
Created on 11 de dez de 2016

@author: rafaelbraga
'''
from business import Business
from SimpleXMLRPCServer import SimpleXMLRPCServer

class RCPServer(object):
    '''
    classdocs
    '''

    def __init__(self, params):
        pass
        '''
        Constructor
        '''

    def getStatus(idsensor): 
        msg = Business.Business().getStatus(idsensor)
        return msg
    
    server = SimpleXMLRPCServer(("localhost", 8000))
    print "Listening on port 8000..."
    server.register_function(getStatus, "getStatus")
    server.serve_forever()
