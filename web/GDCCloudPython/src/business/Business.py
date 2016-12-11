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
    
    @staticmethod
    def getStatus(id_sensor):

        c = Connection.Connection('192.168.0.105', 27017)
        
        if id_sensor == 1:
            sensor1 = c.getSensor1()
            jsondict = sensor1.next()    

            voltage_companhia = jsondict['voltage_companhia'] #companhia

            sensor3 = c.getSensor3()
            last_sensor3 = sensor3.next()
                        
            status = c.getStatusGDC()
            last_status = status.next()
            
            if voltage_companhia > 20 and last_sensor3['voltage_gerador'] > 20:
                last_status['codStatus'] = 0
                last_status['mensagem'] = "O Sistema opera normalmente"

            if voltage_companhia < 20 and last_sensor3['voltage_gerador'] > 20:
                last_status['codStatus'] = 1
                last_status['mensagem'] = "Alerta - Faltou energia da companhia, mas gerador ja esta funcionando"   
                
            if voltage_companhia < 20 and last_sensor3['voltage_gerador'] < 20:
                last_status['codStatus'] = 1
                last_status['mensagem'] = "Alerta - Falta energia completamente"   

                
            del last_status['_id']
            last_status['voltage_companhia'] = voltage_companhia
            last_status['date'] = datetime.datetime.utcnow()
            
            c.setStatus(last_status)
        elif id_sensor == 2:
            sensor2 = c.getSensor2()
            jsondict = sensor2.next()
            
            temperature = jsondict['temperature']
            humidity = jsondict['humidity']

            sensor1 = c.getSensor1()
            last_sensor1 = sensor1.next()
            
            sensor3 = c.getSensor3()
            last_sensor3 = sensor3.next()            
            
            status = c.getStatusGDC()
            last_status = status.next()

            if (temperature >= 20 and temperature <=  22) and (last_sensor3['temperature'] >= 20 and last_sensor3['temperature'] <=  22):
                if (humidity >= 45 and humidity <= 55) and (last_sensor3['humidity'] >= 45 and last_sensor3['humidity'] <= 55):
                    last_status['codStatus'] = 0
                    last_status['mensagem'] = "O Sistema opera normalmente"
                else:
                    last_status['codStatus'] = 1
                    last_status['mensagem'] = "Atencao - Umidade fora do normal"                    
            else:
                last_status['codStatus'] = 1
                last_status['mensagem'] = "Atencao - Temperatura fora do normal"


            if (temperature < 18 or temperature >=  26) and (last_sensor3['temperature'] < 20 or last_sensor3['temperature'] >=  26):
                last_status['codStatus'] = 2
                last_status['mensagem'] = "Alerta - Temepratura muito elevada ou muito baixa"
                                
            if (humidity <= 40 or humidity >= 70) and (last_sensor3['humidity'] <= 40 or last_sensor3['humidity'] >= 70):
                last_status['codStatus'] = 2
                last_status['mensagem'] = "Alerta - Umidade muito elevada ou muito baixa"

            
            
            del last_status['_id']
            last_status['temperature'] = temperature
            last_status['humidity'] = humidity            
            last_status['timestamp'] = datetime.datetime.utcnow()            
            
            c.setStatus(last_status)
        elif id_sensor == 3:
            sensor3 = c.getSensor3()
            jsondict = sensor3.next()            
            
            temperature = jsondict['temperature']
            humidity = jsondict['humidity']
            voltage_gerador = jsondict['voltage_gerador'] #gerador
            
            sensor1 = c.getSensor1()
            last_sensor1 = sensor1.next()
            
            sensor2 = c.getSensor2()
            last_sensor2 = sensor2.next()
            
            status = c.getStatusGDC()
            last_status = status.next()
            
            if (temperature >= 20 and temperature <=  22) and (last_sensor2['temperature'] >= 20 and last_sensor2['temperature'] <=  22):
                if (humidity >= 45 and humidity <= 55) and (last_sensor2['humidity'] >= 45 and last_sensor2['humidity'] <= 55):
                    if voltage_gerador > 20 and last_status['voltage_companhia'] > 20:
                        last_status['codStatus'] = 0
                        last_status['mensagem'] = "O Sistema opera normalmente"
                    else:
                        last_status['codStatus'] = 2
                        last_status['mensagem'] = "Alerta - Faltou energia no gerador"
                else:
                    last_status['codStatus'] = 1
                    last_status['mensagem'] = "Atencao - Umidade fora do normal"
            else:
                last_status['codStatus'] = 1
                last_status['mensagem'] = "Atencao - Temperatura fora do normal"

                
            if (temperature < 18 or temperature >=  26) and (last_sensor2['temperature'] < 20 or last_sensor2['temperature'] >=  26):
                last_status['codStatus'] = 2
                last_status['mensagem'] = "Alerta - Temperatura muito elevada ou muito baixa"
                
            if (humidity <= 40 or humidity >= 70) and (last_sensor2['humidity'] <= 40 or last_sensor2['humidity'] >= 70):
                last_status['codStatus'] = 2
                last_status['mensagem'] = "Alerta - Umidade muito elevada ou muito baixa"   
                    
            if voltage_gerador < 20 and last_sensor1['voltage_companhia'] < 20:
                last_status['codStatus'] = 2
                last_status['mensagem'] = "Alerta - Faltou energia da companhia e do gerador"


            
            del last_status['_id']
            last_status['temperature'] = temperature
            last_status['humidity'] = humidity
            last_status['voltage_gerador'] = voltage_gerador
            last_status['date'] = datetime.datetime.utcnow()
            
            c.setStatus(last_status)
        c.closeConnection()
        return last_status['mensagem']

    def emitirAlerta(self, mensagem):
        print mensagem

    
    def predizStatus(self):
        print 'predicao'



