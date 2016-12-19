'''
Created on 11 de dez de 2016

@author: rafaelbraga
'''
import xmlrpclib

class RCPClient (object):
    '''
    classdocs
    '''

    def __init__(self, params):
        '''
        Constructor
        '''
    #proxy = xmlrpclib.ServerProxy("http://localhost:8000/")
    #print "3 is even: %s" % str(proxy.is_even(3))
    #print "100 is even: %s" % str(proxy.is_even(100))
    
    proxy = xmlrpclib.ServerProxy("http://192.168.0.62:8000/")
    print "Status: %s" % proxy.getStatus(1)