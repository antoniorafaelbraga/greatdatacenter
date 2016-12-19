'''
Created on 21 de nov de 2016

@author: rafaelbraga
'''

from serialgw import SerialGw
from persistence import Connection
from socketclient import SocketGDCClient

if __name__ == '__main__':
    
    #while True:
    for x in range(0, 10):
        ''' 
            Ler dados da interface serialgw
        '''
        print "=============================SerialGw======================="
        s = SerialGw.SerialGw("/dev/ttyUSB0", 9600)
        jsonsensors = s.readSerial()
        print "============================================================"        

        ''' 
            Salva Json no banco de dados
            Servidor local 192.168.56.101  
            Servidor remoto 52.67.30.209 (nuvem amazon)
        '''
        print "=============================BD============================="
        c = Connection.Connection('192.168.1.5', 27017)
        c.insertJsonSensors(jsonsensors)
        print "============================================================"

        
        ''' 
            Define Status do ambiente
        '''
        print "=============================Status========================="
        socket = SocketGDCClient.SocketGDCClient('192.168.0.62', 8000)
        socket.defineStatus()
        print "============================================================"        
        
                
        '''
            Fecha conexao com banco de dados eu mesmo
        '''
        c.closeConnection()
        
        
        
        
        