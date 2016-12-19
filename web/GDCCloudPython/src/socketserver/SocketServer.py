'''
Created on 18 de dez de 2016

@author: rafaelbraga
'''
import socket
from business import Business

''' classdocs '''
class SocketServer(object):

    ''' Constructor '''
    def __init__(self, host, port):
        tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        orig = (host, port)
        tcp.bind(orig)
        tcp.listen(1)
        self.tcpconn = tcp
        
    def defineStatus(self):
        while True:
            print 'Aguardando conexao'
            con, cliente = self.tcpconn.accept()
            print 'Concetado por', cliente
            while True:
                msg = con.recv(1024)
                if not msg: break
                print cliente, msg
                jsonstatus = Business.Business().getStatus(int(msg))
                print jsonstatus
            print 'Finalizando conexao do cliente', cliente
            con.close()
            return msg