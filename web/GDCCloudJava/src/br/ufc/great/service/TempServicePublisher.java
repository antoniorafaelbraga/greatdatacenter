package br.ufc.great.service;

import javax.xml.ws.Endpoint;

public class TempServicePublisher {
    public static void main(String[] args) {
        // 1st argument is the publication URL, 2nd argument is an SIB instance       
        Endpoint.publish("http://192.168.1.52:9876/temp", new TempServiceImpl());
        //To acess the wsdl documento see the link: http://192.168.1.52:9876/temp?wsdl
    } 
} 