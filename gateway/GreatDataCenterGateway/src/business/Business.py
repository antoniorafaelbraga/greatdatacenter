'''
Created on 21 de nov de 2016

@author: rafaelbraga
'''
import datetime
'''
classdocs
'''
class Business(object):

    '''
    Constructor
    '''
    def __init__(self):
        pass
    
    def getStatus(self, jsondict):
        status = 0
        mensagem = ''
        
        temperature = jsondict['temperature']
        humidity = jsondict['humidity']
        voltage = jsondict['voltage']
        print temperature, humidity, voltage

        
        if temperature >= 20 and temperature <=  22:
            if humidity >= 45 and humidity <= 55:
                if voltage == 0:
                    status = 0
                    mensagem = "O Sistema opera normalmente"
                    self.emitirAlerta(mensagem)
        else:
            if temperature < 20 or temperature >=  26:
                if humidity <= 40 or humidity >= 70:
                    if voltage == 1:
                        status = 1
                        mensagem = "O Sistema opera em estado de alerta"
                        self.emitirAlerta(mensagem)

        jsonstatus = {"status" : status, "mensagem" : mensagem, "timestamp" : datetime.datetime.utcnow()}
        return jsonstatus

    def setStatus(self):
        pass
    
    
    def emitirAlerta(self, mensagem):
        print mensagem

    
    def predizStatus(self):
        print 'predicao'



