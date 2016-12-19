'''
Created on 21 de nov de 2016

@author: rafaelbraga
'''
import time
from serialgw import SerialGw
from persistence import Connection
from socketclient import SocketGDCClient

if __name__ == '__main__':
    
    while True:
    #for x in range(0, 3):
        
        start_time = time.time()
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
        c = Connection.Connection('192.168.0.62', 27017)
        c.insertJsonSensors(jsonsensors)
        print "============================================================"

        ''' 
            Define Status do ambiente
        '''
        print "=============================Status========================="
        socketgdc = SocketGDCClient.SocketGDCClient('192.168.0.62', 5000)
        msg = socketgdc.defineStatus(str(jsonsensors['id']))
        print msg
        print "============================================================"        
        
        elapsed_time = time.time() - start_time
        jsontempo = {'elapsed_time': elapsed_time, 'id_sensor': jsonsensors['id'], 'id_banco': jsonsensors['_id']}
        c.insertTimeExecution(jsontempo)
        
        
        '''
            Fecha conexao com banco de dados
        '''
        c.closeConnection()
        
        
