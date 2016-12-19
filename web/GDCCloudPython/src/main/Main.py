'''
Created on 21 de nov de 2016

@author: rafaelbraga
'''

import socket
from business import Business
#from socketserver import SocketServer

if __name__ == '__main__':
    
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    orig = ('', 5000)
    tcp.bind(orig)
    tcp.listen(1)
    tcpconn = tcp    
    
    while True:
        print 'Aguardando conexao'
        con, cliente = tcpconn.accept()
        print 'Concetado por', cliente
        while True:
            msg = con.recv(1024)
            if not msg: break
            print cliente, msg
            jsonstatus = Business.Business().getStatus(int(msg))
            print jsonstatus
        print 'Finalizando conexao do cliente', cliente
        con.close()
   
    #so = SocketServer.SocketServer('', 5000)
    #msg = so.defineStatus()
    #print msg