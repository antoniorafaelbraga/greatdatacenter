package br.ufc.great.service;

import javax.jws.WebMethod;
import javax.jws.WebService;
import javax.jws.soap.SOAPBinding;

import br.ufc.great.model.GreatDataCenter;

@WebService(targetNamespace = "http://192.168.0.103:9876/GreatDataCenter/GDCWSDL")
@SOAPBinding(style = SOAPBinding.Style.RPC)
public interface GDCService {

	@WebMethod
	public GreatDataCenter getGDC();
	
	@WebMethod
	public float getTemperature();

	@WebMethod
	public float getHumidity();
	
	@WebMethod
	public int getVoltage();
	
	@WebMethod
	public int getStatus();
}
