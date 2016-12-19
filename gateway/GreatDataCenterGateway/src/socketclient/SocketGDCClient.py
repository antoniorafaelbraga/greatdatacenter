'''
Created on 19 de dez de 2016

@author: rafaelbraga
'''

import socket

''' classdocs '''
class SocketGDCClient(object):

    '''  Constructor  '''
    def __init__(self, server, port):
        tcpconnection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        dest = (server, port)
        tcpconnection.connect(dest)
        
        self.tcpconnection = tcpconnection
        print "Conexao TCP estabelecida via socket"


    def defineStatus(self, idsensor):
        self.tcpconnection.send (idsensor)
        self.tcpconnection.close()