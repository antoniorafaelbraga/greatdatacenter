'''
Created on 18 de dez de 2016

@author: rafaelbraga
'''

import time
from persistence import Connection

class MyClass(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
    
    c = Connection.Connection('192.168.1.5', 27017)
    cursor = c.getCursorLog()
    while cursor.alive:
        try:
            doc = cursor.next()
            print doc
        except StopIteration:
            time.sleep(1)