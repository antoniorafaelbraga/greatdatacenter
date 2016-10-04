package br.ufc.great.service;

import javax.jws.WebMethod;
import javax.jws.WebService;
import javax.jws.soap.SOAPBinding;

@WebService(targetNamespace = "http://192.168.1.52:9876/temp/wsdl")
@SOAPBinding(style = SOAPBinding.Style.RPC)
public interface TempService {
	@WebMethod
	public float getTempC() throws java.io.IOException, java.lang.InterruptedException;

	@WebMethod
	public float getTempF() throws java.io.IOException, java.lang.InterruptedException;
}