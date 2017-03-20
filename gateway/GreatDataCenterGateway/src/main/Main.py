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
        ''' 
            Ler dados da interface serialgw
        '''
        print "=============================SerialGw======================="
        start_time = time.time()
        s = SerialGw.SerialGw("/dev/ttyUSB0", 9600)
        jsonsensors = s.readSerial()
        time_sensor = time.time() - start_time
        print "============================================================"

        ''' 
            Salva Json no banco de dados
        '''
        print "=============================BD============================="
        start_time = time.time()
        c = Connection.Connection('192.168.0.62', 27017)
        c.insertJsonSensors(jsonsensors)
        time_bd = time.time() - start_time
        print "============================================================"
        
        ''' 
            Define Status do ambiente
        '''
        print "=============================Status========================="
        start_time = time.time()
        socketgdc = SocketGDCClient.SocketGDCClient('192.168.0.62', 5000)
        socketgdc.defineStatus(str(jsonsensors['id']))
        time_status = time.time() - start_time
        print "============================================================"
        
        '''
            Salva tempos de execução e fecha conexao com banco de dados
        '''
        print "=============================Log============================"
        jsontempo = {'id_banco': jsonsensors['_id'], 'time_sensor': time_sensor, 'time_bd': time_bd, 'time_status': time_status}
        c.insertTimeExecution(jsontempo)
        c.closeConnection()
        print "=============================Log============================"        
        
