package br.ufc.great.service;
import java.io.IOException;
import java.io.InputStreamReader;
import javax.jws.WebService;

@WebService(name = "temp", serviceName = "tempService", portName= "tempPort",
targetNamespace = "http://192.168.1.52:9876/temp/wsdl", endpointInterface = "TempService")
public class TempServiceImpl implements TempService {
	@Override
	public float getTempC() throws java.io.IOException, java.lang.InterruptedException {
		// Get runtime
		java.lang.Runtime rt = java.lang.Runtime.getRuntime();
		// Start a new process & run python
		// Use Python to access TMP102 sensor
		java.lang.Process p = rt.exec("/usr/bin/python /home/root/tmp102.py");
		// wait for the process to complete
		p.waitFor();
		// Get process output - its InputStream
		java.io.InputStream is = p.getInputStream();
		java.io.BufferedReader reader = new java.io.BufferedReader(new InputStreamReader(is));
		// And print each line
		String s = null;
		s = reader.readLine();
		return Float.parseFloat(s);
	}

	@Override
	public float getTempF() throws IOException, InterruptedException {
		float c = getTempC();
		return ((c / 5) * 9) + 32;
	}
}