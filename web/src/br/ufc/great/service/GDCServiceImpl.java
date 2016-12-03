package br.ufc.great.service;

import javax.jws.WebService;

import br.ufc.great.model.GreatDataCenter;

@WebService(name = "gdc", serviceName = "gdcService", portName= "gdcPort",
targetNamespace = "http://192.168.0.103:9876/GreatDataCenter/GDCWSDL", endpointInterface = "GDCService")
public class GDCServiceImpl implements GDCService {

	@Override
	public GreatDataCenter getGDC() {

		
		
		
		
		return null;
	}

	@Override
	public float getTemperature() {
		// TODO Auto-generated method stub
		return 0;
	}

	@Override
	public float getHumidity() {
		// TODO Auto-generated method stub
		return 0;
	}

	@Override
	public int getVoltage() {
		// TODO Auto-generated method stub
		return 0;
	}

	@Override
	public int getStatus() {
		// TODO Auto-generated method stub
		return 0;
	}
	
	

}
