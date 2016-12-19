#!/usr/bin/env python
'''
Created on 17 de dez de 2016

@author: rafaelbraga
'''

from business import Business
from flask import Flask, request

class RPCServer(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''

    app = Flask(__name__)
    
    @app.route("/GDCcloud")
    def getStatus():
        idsensor = request.args.get("idsensor")
        idsensor = int(idsensor)
        msg = Business.Business().getStatus(idsensor)
        return msg, 200
    
    app.run()        