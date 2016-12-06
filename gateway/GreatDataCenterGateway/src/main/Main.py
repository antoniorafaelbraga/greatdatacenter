'''
Created on 21 de nov de 2016

@author: rafaelbraga
'''
from serialgw import SerialGw
from persistence import Connection
from business import Business

if __name__ == '__main__':
    
    #while True:
    #for x in range(0, 2):
        ''' 
            Ler dados da interface serialgw
        '''
        print "=============================SerialGw========================="
        s = SerialGw.SerialGw("/dev/ttyUSB0", 9600)
        jsonsensors = s.readSerial()
        print "============================================================"        

        ''' 
            Salva Json no banco de dados
            Servidor local 192.168.56.101  
            Servidor remoto 52.67.30.209 (nuvem amazon)
        '''
        print "=============================BD============================="
        c = Connection.Connection('52.67.87.15', 27017)
        c.insertJsonSensors(jsonsensors)
        print "============================================================"        

        '''
            Define status do ambiente
        '''
        print "=============================Status========================="
        jsonstatus = Business.Business().getStatus(jsonsensors)
        print "============================================================"
        
        '''
            Faz analise preditiva do estado do sistema
        '''
        print "=============================Predicao======================="
        jsonpredicao = Business.Business().predizStatus()
        print "============================================================"
                
        '''
            Fecha conexao com banco de dados
        '''
        c.closeConnection()
        
        
        
        
        