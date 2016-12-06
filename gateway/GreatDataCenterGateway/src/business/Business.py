'''
Created on 21 de nov de 2016

@author: rafaelbraga
'''
import datetime
from persistence import Connection
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

        c = Connection.Connection('52.67.87.15', 27017)
        id_sensor = jsondict['id']
        
        if id_sensor == 1:
            voltage_companhia = jsondict['voltage_companhia'] #companhia
            status = c.getStatusGDC()
            last_status = status.next()
            
            if voltage_companhia > 20 and last_status['voltage_gerador'] > 20:
                last_status['codStatus'] = 0
                last_status['mensagem'] = "O Sistema opera normalmente"
                last_status['date'] = datetime.datetime.utcnow()
            elif voltage_companhia < 20 and last_status['voltage_gerador'] > 20:
                last_status['codStatus'] = 1
                last_status['mensagem'] = "Sistema em estado de alerta - Faltou energia da companhia"   
                last_status['date'] = datetime.datetime.utcnow()
            del last_status['_id']
            c.setStatus(last_status)
        elif id_sensor == 2:
            temperature = jsondict['temperature']
            humidity = jsondict['humidity']
            status = c.getStatusGDC()
            last_status = status.next()

            if (temperature >= 20 and temperature <=  22) and (last_status['temperature'] >= 20 and last_status['temperature'] <=  22):
                if (humidity >= 45 and humidity <= 55) and (last_status['humidity'] >= 45 and last_status['humidity'] <= 55):
                    last_status['codStatus'] = 0
                    last_status['mensagem'] = "O Sistema opera normalmente"
                    last_status['timestamp'] = datetime.datetime.utcnow()
            else:
                if (temperature < 20 or temperature >=  26) and (last_status['temperature'] < 20 or last_status['temperature'] >=  26):
                    if (humidity <= 40 or humidity >= 70) and (last_status['humidity'] <= 40 or last_status['humidity'] >= 70):
                        status['codStatus'] = 1
                        status['mensagem'] = "Sistema em estado de alerta - Temperatura acima da normal"
                        status['timestamp'] = datetime.datetime.utcnow()
            del last_status['_id']
            c.setStatus(last_status)
        elif id_sensor == 3:
            temperature = jsondict['temperature']
            humidity = jsondict['humidity']
            voltage_gerador = jsondict['voltage_gerador'] #gerador
            status = c.getStatusGDC()
            last_status = status.next()
            
            if (temperature >= 20 and temperature <=  22) and (last_status['temperature'] >= 20 and last_status['temperature'] <=  22):
                if (humidity >= 45 and humidity <= 55) and (last_status['humidity'] >= 45 and last_status['humidity'] <= 55):
                    if voltage_gerador > 20 and status['voltage_companhia'] > 20:
                        last_status['codStatus'] = 0
                        last_status['mensagem'] = "O Sistema opera normalmente"
                        last_status['voltage_gerador'] = 1
                        last_status['timestamp'] = datetime.datetime.utcnow()
                else:
                    if (temperature < 20 or temperature >=  26) and (last_status['temperature'] < 20 or last_status['temperature'] >=  26):
                        if (humidity <= 40 or humidity >= 70) and (last_status['humidity'] <= 40 or last_status['humidity'] >= 70):
                            if voltage_gerador < 20 and status['voltage_companhia'] > 20:
                                last_status['codStatus'] = 1
                                last_status['mensagem'] = "Sistema em estado de alerta - Faltou energia na companhia"   
                                last_status['voltage_gerador'] = 0
                                last_status['timestamp'] = datetime.datetime.utcnow()
            del last_status['_id']
            c.setStatus(last_status)
        c.closeConnection()
        return ""

    def emitirAlerta(self, mensagem):
        print mensagem

    
    def predizStatus(self):
        print 'predicao'



