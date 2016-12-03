package br.ufc.great.service;

import javax.xml.ws.Endpoint;

/**
 * 
 * @author rafaelbraga
 * 
 * To acess the wsdl documento see the link: http://192.168.0.103:9876/GreatDataCenter/GDCWSDL?wsdl
 * 
 */
public class GDCServicePublisher {
    public static void main(String[] args) {
    	Endpoint.publish("http://192.168.0.103:9876/GreatDataCenter/GDCWSDL", new TempServiceImpl());
    } 
}