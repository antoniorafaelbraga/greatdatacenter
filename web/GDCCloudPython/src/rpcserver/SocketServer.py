'''
Created on 18 de dez de 2016

@author: rafaelbraga
'''
import socket

class MyClass(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        
    HOST = ''              # Endereco IP do Servidor
    PORT = 5000            # Porta que o Servidor esta
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    orig = (HOST, PORT)
    tcp.bind(orig)
    tcp.listen(1)

    while True:
        con, cliente = tcp.accept()
        print 'Concetado por', cliente
        while True:
            msg = con.recv(1024)
            if not msg: break
            print cliente, msg
        print 'Finalizando conexao do cliente', cliente
        con.close()