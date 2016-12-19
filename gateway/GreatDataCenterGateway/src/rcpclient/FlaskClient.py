'''
Created on 17 de dez de 2016

@author: rafaelbraga
'''
import urllib2

class FlaskClient (object):
    '''
    classdocs
    '''

    def __init__(self, params):
        '''
        Constructor
        '''
        
    re = urllib2.urlopen("http://192.168.0.62:5000/GDCcloud?idsensor=1").read()
    print re      