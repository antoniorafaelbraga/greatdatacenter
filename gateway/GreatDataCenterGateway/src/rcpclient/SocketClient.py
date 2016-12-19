'''
Created on 18 de dez de 2016

@author: rafaelbraga
'''

import socket

if __name__ == '__main__':
        
        
    #def socketConn(self):    
        HOST = '192.168.0.62'     # Endereco IP do Servidor
        PORT = 5000            # Porta que o Servidor esta
        tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        dest = (HOST, PORT)
        tcp.connect(dest)
        print 'Para sair use CTRL+X\n'
        msg = raw_input()
        while msg <> '\x18':
            tcp.send (msg)
            msg = raw_input()
        tcp.close()