'''
Created on 21 de nov de 2016

@author: rafaelbraga
'''
import ast
import serial
import datetime

class SerialGw(object):
    '''
    classe responsavel por ler dados da interface serialgw. 
    '''

    def __init__(self, porta, baudrate):
        self.porta = porta
        self.baudrate = baudrate
        
    def readSerial(self):
        ser = serial.Serial(self.porta, self.baudrate)
        ser.flush()
        json = ser.readline()
        jsonsensors = ast.literal_eval(json)
        print json
        jsonsensors.update({"date": datetime.datetime.utcnow()})
        
        #jsonsensors = {'id': 1, 'voltage_companhia': 50, 'date': datetime.datetime.utcnow()}
        #jsonsensors.update({"date": datetime.datetime.utcnow()})
        #jsonsensors = {'id': 2, 'temperature': 21.0, 'humidity': 50.0, 'date': datetime.datetime.utcnow()}
        #jsonsensors = {'id': 3, 'temperature': 21.0, 'humidity': 50.0, 'voltage_gerador': 70, 'date': datetime.datetime.utcnow()}
        print jsonsensors  
        return jsonsensors