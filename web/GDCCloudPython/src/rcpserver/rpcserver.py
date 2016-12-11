'''
Created on 11 de dez de 2016

@author: rafaelbraga
'''
from SimpleXMLRPCServer import SimpleXMLRPCServer

class RCPServer(object):
    '''
    classdocs
    '''

    def __init__(self, params):
        '''
        Constructor
        '''
    
    def is_even(n):
        return n % 2 == 0
    
    server = SimpleXMLRPCServer(("localhost", 8000))
    print "Listening on port 8000..."
    server.register_function(is_even, "is_even")
    server.serve_forever()
